"""
--------------------------------------------------------------------------
6 Finger Augmentation
--------------------------------------------------------------------------
License:   
Copyright 2022 Paul Kim

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
may be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use the following hardware components to make a programmable combination lock: 
  - HT16K33 Display
  - Button
  - Red LED
  - Green LED
  - Potentiometer (analog input)
  - Servo

Requirements:
  - Hardware:
    - When locked:   Red LED is on; Green LED is off; Servo is "closed"; Display is unchanged
    - When unlocked: Red LED is off; Green LED is on; Servo is "open"; Display is "----"
    - Display shows value of potentiometer (raw value of analog input divided by 8)
    - Button
      - Waiting for a button press should allow the display to update (if necessary) and return any values
      - Time the button was pressed should be recorded and returned
    - User interaction:
      - Needs to be able to program the combination for the “lock”
        - Need to be able to input three values for the combination to program or unlock the “lock”
      - Combination lock should lock when done programming and wait for combination input
      - If combination is unsuccessful, the lock should go back to waiting for combination input
      - If combination was successful, the lock should unlock
        - When unlocked, pressing button for less than 2s will re-lock the lock; greater than 2s will allow lock to be re-programmed

Uses:
  - HT16K33 display library developed in class
    - Library updated to add "set_digit_raw()", "set_colon()"

"""
import time

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM

import ht16k33 as HT16K33
import servo as SERVO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class finger_aug():
    """ 6 Finger Augmentation """
    reset_time = None
    button     = None
    red_led    = None
    green_led  = None
    analog_in  = None
    servo      = None
    display    = None
    value      = None

    def __init__(self, reset_time=2.0, button="P2_2",
                       red_led="P2_6", green_led="P2_4",
                       analog_in="P1_19", servo="P1_36",
                       i2c_bus=1, i2c_address=0x70):
        """ Initialize variables and set up display """
        self.reset_time = reset_time
        self.button     = button
        self.red_led    = red_led
        self.green_led  = green_led
        self.analog_in  = analog_in
        self.servo      = SERVO.Servo(servo)
        self.display    = HT16K33.HT16K33(i2c_bus, i2c_address)
        self._setup()
   
    # End def
   
   
    def _setup(self):
        """Setup the hardware components."""

        # Initialize Button
        GPIO.setup(self.button, GPIO.IN)
        # Initialize LEDs
        GPIO.setup(self.red_led, GPIO.OUT)
        GPIO.setup(self.green_led, GPIO.OUT)
       
        # Initialize Analog Input
        ADC.setup()
       
 
    # End def


    def show_analog_value(self):
        """Show the analog value on the screen:
               - Read raw analog value
               - Divide by 4 (remove two LSBs)
               - Display value
               - Return value
        """
       
        # Read raw value from ADC
        value = ADC.read_raw(self.analog_in)
       
        # Divide value by 8
        value = int(value // 16)
       
        
        # Calculate for the "Level" of activity (0~7, 0 = no grip ,5 = max grip)
        val = str(abs(int(self.duty_cycle_calc(value))-8))
        comb = str("ON"+val)
        
        if (self.value != value):
            # Font characterization
            self.display.set_colon(True)
            # Update display ("ON"+integer)
            self.display.text(comb)
            time.sleep(0.1)
            
        self.value = value
       
        # Return value
        return value

    # End def
    
    def duty_cycle_calc(self, number):
        """Calculate the "level" of grip that is being applied."""
        # Calculate for relevant duty cycle. May change with potentiometer and servo used
        calc = (number/50)+3
        
        # Return Value
        return calc
    # End def





    def run(self):
        """Execute the main program."""

        while(1):
            # Show "ON" state via green led
            GPIO.output(self.green_led, GPIO.HIGH)
           
            # Measure the variable analog value generated by potentiometer
            combination = self.show_analog_value()
            
            # Calculate
            duty_cycle=self.duty_cycle_calc(combination)
            self.servo.scale(duty_cycle)
            
            # Off status with button press
            if (GPIO.input(self.button) == 0):
                
                
                # Return servo to no-tension state
                self.servo.scale(8.5)
                # Show "ON" state via text and red led
                self.display.text("OFF")
                GPIO.output(self.green_led, GPIO.LOW)
                GPIO.output(self.red_led, GPIO.HIGH)
                break

    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
       
        # Set Display to something fun to show program is complete
        self.display.text("DEAD")
        self.display.set_colon(False)

        # Clean up GPIOs
        GPIO.output(self.red_led, GPIO.LOW)
        GPIO.output(self.green_led, GPIO.LOW)

        # Clean up GPIOs
        GPIO.cleanup()

        # Stop servo
        self.servo.cleanup()

    # End def

# End class


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    fin_aug = finger_aug()

    try:
        # Run the lock
        fin_aug.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        fin_aug.cleanup()

    print("Program Complete")