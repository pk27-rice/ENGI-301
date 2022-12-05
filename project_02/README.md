--------------------------------------------------------------------------
PCB for 6 Finger Augmentation with BeagleBone
--------------------------------------------------------------------------

--------------------------------------------------------------------------
https://www.hackster.io/pkim7035/6-finger-augmentation-with-beaglebone-d0ea5d
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

**Description:**
In this project, a **PCB** for a device with variable grip for a 6 finger augmentation device is possible through 
the use of a servo and potentiometer has been developed.

A 6 finger augmentation device was generated through the modification to existing 3D-printed prosthetic hand to develop 
a 6th finger prosthetic augmentation in a form of a thumb that attaches to the side of the hand. 
This project was made with a focus on allowing for a variable grip to reduce the difficulty in grabbing larger objects 
or holding multiple smaller objects. The STLs for this project was generated through the modification of the existing 
e-NABLE Phoenix hand design.

This project uses the variable resistance allowed by potentiometer for increased control of the finger movement and 
can easily be replaced with strain gauges orelectronic components that allows for variable resistance. Further development 
in ergonomic considerations is needed in the forms of changing print design to allow for TPA material to improve fit, 
optimizing servo location/ wiring to increase usability, and modifying phalanx/fingertip length and surface to improve grip.


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

**Credit**      
     -Special thanks to Eric Welsh who guided learning and project development
     
