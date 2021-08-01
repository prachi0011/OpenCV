# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:15:03 2021

@author: HP
"""

##screen recorder
import cv2
import pyautogui
import imutils
import numpy as np
import time


print("Welcome to Screen Recorded")
recording_style =int(input("Please type 1 if you want to record screen and if want to record screen for \
                        duration of time type 2 and hit 'Enter':   "))

if recording_style == 1:
    # display screen resolution, get it from your OS settings
    print("Give screen resolution")
    h = int(input("height: "))
    w = int(input("Width: "))#(1366, 768) -- screen size for my system (width, hieght)
   #("Write your complete directory and file name with extension .avi")
    
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter("E:\\Prachi Agrawal\\Big Data JoVAC\\Images\\screenrecorddur.avi", fourcc, 20.0, (w,h))
    while True:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        
        out.write(frame)
        cv2.imshow("screen", imutils.resize(frame, (600)))
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break
        
    # Release everything if job is finished
    out.release()
    
##recordscreen for limited time
if recording_style == 2:
    #Screen_size = (width, height)
   #("Write your complete directory and file name")
    print("Give screen resolution")
    h = int(input("height: "))
    w = int(input("Width: "))
    print("To stop recording on video press q")
    dur = int(input("time duration: "))
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter("E:\\Prachi Agrawal\\Big Data JoVAC\\Images\\screenrecorddur.avi", fourcc, 20.0, (w,h))
    start_time = time.time()
    while(int(time.time() - start_time) < dur):
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
        out.write(frame)
        cv2.imshow("Frame", imutils.resize(frame, (800)))
        if cv2.waitKey(1) == ord("q"):
            break
    out.release()

print("Screen has been recorded!")
cv2.destroyAllWindows()