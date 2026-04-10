#!/usr/bin/python3
#
# Copyright (c) 2014 OpenElectrons.com
# Pi-Pan isntallation script.
# for more information about Pi-Pan,  please visit:
# http://www.openelectrons.com/Pi-Pan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author         Comments
# 08/22/13  Deepak         Initial authoring.
# 08/04/14  Michael Giles  Doxygen
# 01/22/23  Rob Cooklock   Updated to use PCA9685 16 channel servo controller
#
# this is driver for the Openelectrons.com PiPan  
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit
TiltServo = 1
PanServo = 0

## PiPan: this class provides functions for PiPan servo controller
#  for read and write operations.
class PiServo:
    
    x = 90
    y = 90

    ## Initialize the class by opening servoblaster
    #  @param self The object pointer.
    def __init__(self):
        global kit
        try:
            kit = ServoKit(channels=8)
            kit.frequency = 60
            #self.test_servos()
            self.neutral_pan()
            self.neutral_tilt()
        except (IOError):
            print ("*** ERROR ***")
            print ("Unable to open the device, check that PCA9685 is connected")
            exit()

    ## Writes a pwm value one of the servo controller pins
    #  @param self The object pointer.
    #  @param pin The servo number at which to write.
    #  @param angle The angle to write to the desired pin.
    def pwm(self, servo, angle):
        #print ("servo[" + str(servo) + "][" + str(angle) + "]")
        kit.servo[servo].angle = angle

    ## Brings tests both servos to brings to neutral position
    #  @param self The object pointer.
    def test_servos(self):
        # Set channels to the number of servo channels on your kit.
        # Test servos set to neutral position.
        kit.servo[PanServo].angle = 0
        kit.servo[TiltServo].angle = 0
        time.sleep(1)
        kit.servo[PanServo].angle = 180
        kit.servo[TiltServo].angle = 180
        time.sleep(1)
        kit.servo[PanServo].angle = 0
        kit.servo[TiltServo].angle = 0
        time.sleep(1)
        kit.servo[PanServo].angle = 90
        kit.servo[TiltServo].angle = 90

    ## Brings the pan servo to neutral position
    #  @param self The object pointer.
    def neutral_pan(self):
        self.pwm (PanServo, int(90))

    ## Brings the tilt servo to neutral position
    #  @param self The object pointer.
    def neutral_tilt(self):
        self.pwm (TiltServo, int(90))

    ## Writes pan movement value between 0 and 180
    #  @param self The object pointer.
    def do_pan(self, x):
        if ( x > 180 ):
            x = 180
        if ( x < 0 ):
            x = 0
        self.pwm (PanServo, int(x))

    # Writes the tilt movement value between 0 and 180
    #  @param self The object pointer.
    def do_tilt(self, y):
        # limit tilt between 0 and 180
        if ( y > 180 ):
            y = 180
        if ( y < 0 ):
            y = 0
        self.pwm (TiltServo, int(y))



