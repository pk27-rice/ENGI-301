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

Use the following hardware components to make a programmable 6 finger augmentation: 
  - HT16K33 Display
  - Button
  - Red LED
  - Green LED
  - Potentiometer (analog input)
  - Servo

**Requirements:**
  **- Hardware:**
    - When Off: Red LED is on; Green LED is off; Servo is returned to Grip level 0 with no line tension; Display is "OFF"
    - When Operational: Red LED is off; Green LED is on; Servo is "open"; Display is "ON: Grip Level"
    - Display number shows value of grip level (0~5, 0 = no grip ,5 = max grip)
    - Button
      - Any button press will turn off the device
    - Potentiometer
      - Potentiometer can be adjsted to change the "Grip Level"
    - User interaction:
      - Needs to be able to adjust the potentiometer to adjust the grip of the finger
      - User is able to see the level of grip and state of machine on the LCD
      - In any state, pressing button will disable the device and return the grip state to 0
      
**Build Instruction:**
Assembly of Hand and Servo:
Please refer to the following link for images as needed (https://www.hackster.io/pkim7035/6-finger-augmentation-with-beaglebone-d0ea5d)

From the build process of the base e-NABLE Phoenix hand, only the thumb needs to be assembled.

1) Identification of Parts
  1. Orthodontic Elastic Rubber Band (3/16’’)
  2. Fishing Line
  3. thumb_knuckle_pin.stl
  4. finger_phalanx.stl
  5. thumbtip_pin.stl
  6. fingertip_short_v2.stl
  7. 6 Finger_v2.stl
  8. Velcro Straps (12’’ x 1/2’’)
  9. SG90 Servo

2) Assembling the Fingers
  a. Gather the following pieces:
    4. finger_phalanx.stl
    5. thumbtip_pin.stl
    6. fingertip_short_v2.stl
  b. Assemble the thumb by aligning the rectangular holes in pieces 4. finger_phalanx.stl and 6. fingertip_short_v2.stl
  c. Insert piece 5. thumbtip_pin.stlin the rectangular hole and push in completely to generate the 4,5.6 Thumb piece

3) Attaching the Fingers
  a. Gather the following pieces:
    4,5,6 Thumb piece
    3. thumb_knuckle_pin.stl
    7. 6 Finger_v2.stl
  b. Assemble the thumb by aligning the rectangular holes in pieces 4,5,6. Thumb piece and 7. 6 Finger_v2.stl
  c. Insert piece 3. thumb_knuckle_pin.stl in the rectangular hole and push in completely to finish the assembly of the 6 finger augmentation device

4) Applying the Dental Bands
  a. Gather the following pieces:
    3,4,5,6,7. 6 finger augmentation device
    1. Orthodontic Elastic Rubber Band (3/16’’)
  b. Attach the rubber bands to both joints outlined in yellow
  
5) Securing the Servo motor
  a. Gather the following pieces:
    1,3,4,5,6,7. 6 finger augmentation device
    9. SG90 servo
  b. Attach the servo from the bottom up on the slot outlined in yellow
  c. Secure the servo to the 6 finger augementation device by screwing in the Phillips screw that comes with the SG90 servo.
  
6) Stringing the Fingers to the Servo Motor
  a. Gather the following pieces:
    1,3,4,5,6,7,9. 6 finger augmentation device
    2. Fishing Line
  b. After knotting the fishing line to the end of the servo wing, follow the instruction online for stringing the thumb.
  
7) Inputting the Velcro Strips
  a. Insert Velcro strips on the slots outlined in yellow
  b. This marks the end of assembly
      
**Operation Instruction:**
Please refer to the following link for images as needed (https://www.hackster.io/pkim7035/6-finger-augmentation-with-beaglebone-d0ea5d)

1. Attachment to Hand
  -The Velcro strip further from the servo should wrap around the palm of the hand
  -The Velcro strip near the servo should wrap around the wrist of the hand
  
2. Adjusting the Potentiometer to Manage Grip
  -There is an initial grip of the finger with the device's startup to show if the program is working properly
  -Adjusting the resistance with the potentiometer will change the grip level
  
3. Reading the LCD Screen / LED
  - The LCD should update with the potentiometer adjustment to show (ON : "Grip level")
  - The Grip level is a 0 - 5 scale with 0 = no grip & 5 = maximum possible grip
  - The green LED will light up to signify operation

4. Turning Off the Device
  - Press the button to end operation
  - The LCD should update to show (OFF)
  - The red LED will light up to signify end of operation
      
      
"""
