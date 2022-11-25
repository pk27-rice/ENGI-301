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
    - When Off:   Red LED is on; Green LED is off; Servo is returned to Grip level 0 with no line tension; Display is "OFF"
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
      
"""
