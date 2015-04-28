# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:21:10 2015

@author: bernard
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
ser = serial.Serial('/dev/ttyUSB1', 115200)

ser.write('X0 Y0 Z')