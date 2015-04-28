# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:27:12 2015

@author: raphael
"""
import io
import time
import picamera
import cv2
import numpy as np

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')

data = np.fromstring(stream.getvalue(), dtype=np.uint8)

image = cv2.imdecode(data, 1)

image = image[:, :, ::-1]

print image[0][1]