#varrock fireman
print('bobo')

import cv2 as cv
from cv2 import threshold
from cv2 import _InputArray_STD_BOOL_VECTOR
import numpy as np
import os
from windmouse import wind_mouse
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from pyHM import Mouse
import time
from action import Action
import breakRoller


#notes
#this depends on inventory keybind set to f1, magic to f2, and escape to close interfaces. None of that is standard.
#move your logs aroudn in bank
#move your 2 tinder boxes aruond in inventory
#take new in_bank_vision
#take new bank image
#make new bank mask
#update bank mask dimensions in bank action
#this really only works in resizable modern with a big bank snapshot. 
#must click on to runelite window before countdown completes, otherwise the hotkeys won't work. 
#falador minimap mask requires you be in resizable modern with full health and 0 prayer. rund oesn't matter
#in order for fally minimap to work, the window must be 
#to improve


# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Vessacks')
#wincap = WindowCapture('full_window.PNG - Paint')

# initialize the Vision class
inv_log_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log_search_mask.png',0)
inv_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask= inv_log_search_mask)

tinder_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder_search_mask.png',0)
tinder_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask = tinder_search_mask)

falador_minimap_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap_search_mask.png',cv.IMREAD_GRAYSCALE)
falador_minimap_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask = falador_minimap_search_mask)

bank_minimap_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
in_bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\in_bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)

bank_log_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log_search_mask.png',0)
bank_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask = bank_log_search_mask)

varrock_tele_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\varrock_tele_search_mask.png',0)
varrock_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\varrock_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask= varrock_tele_search_mask)

falador_tele_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele_search_mask.png',0)
falador_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask= falador_tele_search_mask)

lumbridge_tele_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele_search_mask.png',0)
lumbridge_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask= lumbridge_tele_search_mask)


#initialize the action class
falador_tele_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele_click_mask.png',0)
falador_tele_face_size = [20,20]
falador_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele.png', click_mask = falador_tele_click_mask, face_size = falador_tele_face_size)

varrock_tele_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\varrock_tele_click_mask.png',0)
varrock_tele_face_size = [20,20]
varrock_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\varrock_tele.png', click_mask = varrock_tele_click_mask, face_size = varrock_tele_face_size)

lumbridge_tele_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele_click_mask.png',0)
lumbridge_tele_face_size = [20,20]
lumbridge_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele.png', click_mask = lumbridge_tele_click_mask, face_size = lumbridge_tele_face_size)

bank_log_face_size = [31,28]
bank_log_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log_click_mask.png',0)
bank_log_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log.png',click_mask = bank_log_click_mask, face_size = bank_log_face_size)

#inv_log_face_size = [31,28]
#inv_log_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log_click_mask.png',0)
inv_log_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png')

tinder_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png')

falador_minimap_face_size = [48,93]
falador_minimap_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap_click_mask.png',0)
falador_minimap_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap.png', click_mask= falador_minimap_click_mask, face_size= falador_minimap_face_size)

bank_minimap_face_size = [29,29]
bank_minimap_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap_click_mask.png',0)
bank_minimap_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap.png', click_mask= bank_minimap_click_mask, face_size= bank_minimap_face_size) #note: i'm eyeballing this size. take a look if it causes problems

bank_face_size = [250,88]
bank_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_click_mask.png',0)
bank_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png', click_mask= bank_click_mask, face_size= bank_face_size) #note: with a zone this small, there may be no room to walk



#constants
RUNE_THRESHOLD = .85
TELE_THRESHOLD = .92
FALADOR_MINIMAP_THRESHOLD = .6
BANK_MINIMAP_THRESHOLD =.7
BANK_THRESHOLD = .57
IN_BANK_THRESHOLD =.85
BANK_LOG_THRESHOLD = .75
INV_LOG_THRESHOLD = .80
TINDER_THRESHOLD = .80

#some functions: 

def speed():
    speed = np.random.normal(.7,.3)
    while speed > .85 or speed < .6:
        speed = np.random.normal(.75,.08)
    return speed

def tick_dropper(odds=100):
    if np.random.randint(0,odds) == 1:
        time.sleep(.6)

def wait():
    wait = (.1 + abs(np.random.normal(.05,.05)))
    return wait



start_time = time.time()
last_click_time = time.time()
while True:
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    cv.imshow('haystack',screenshot)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()
    
    needle = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap.png',cv.IMREAD_GRAYSCALE)
    cv.imshow('needle', needle)

    cv.imshow('mask', falador_minimap_search_mask)

    falador_minimap_all_points, falador_minimap_best_point, falador_minimap_confidence = falador_minimap_vision.find(screenshot, threshold = FALADOR_MINIMAP_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()

    print('looking for falador minimap | search time %s | confidence %s ' % (time.time()- start_time, falador_minimap_confidence))

