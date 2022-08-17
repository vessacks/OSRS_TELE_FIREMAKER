#varrock fireman

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


# initialize the Vision class
inv_log_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log_search_mask.png',0)
inv_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask= inv_log_search_mask)

tinder_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder_search_mask.png',0)
tinder_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE, search_mask = tinder_search_mask)

falador_minimap_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap_search_mask.png',0)
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

#note: this one IS IN COLOR! when searching for it you must remove the blacka nd white conversion of screenshot first. 
firemaking_xp_search_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\firemaking_xp_search_mask.png',cv.IMREAD_COLOR)
firemaking_xp_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\firemaking_xp.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask = firemaking_xp_search_mask)

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
FIREMAKING_XP_THRESHOLD = .99
#blindness border is a windowcoord y value above which we will pretend to not see xp drops. its needed to create periods with no visible xp drops to time clicks.
#note: i'm pretty sure I'm not using the blindness border rn. I leave it in because other htings call on it, but I don't htink it really helps. 
BLINDNESS_BORDER = 0 # 185 is ok for a full screen on y axis on my samsung monitor. I'm setting it to zero for testing purposes.

teleport_location = 'falador'
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
    wait = (.14 + abs(np.random.normal(.05,.05)))
    return wait


#this function takes you to falador bank and restocks
def restock():
  

    print('entering restock cycle')

    #open magic tab
    time.sleep(wait())
    tick_dropper()
    pyautogui.keyDown('f2')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f2')
    print('clicked f2 to open magic menu')
    #time.sleep(.4 + abs(np.random.normal(.1,.05)))

    start_time = time.time()
    last_click_time = time.time()
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        falador_tele_all_points, falador_tele_best_point, falador_tele_confidence = falador_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        print('looking for falador tele')
        
        if falador_tele_confidence > TELE_THRESHOLD:
            print('found falador tele | confidence %s' % falador_tele_confidence)
            break
        if time.time() - last_click_time > .7:
            last_click_time = time.time()
            print('looked for %s | no falador tele found | confidence %s | re-opening magic tab' % (time.time() - start_time, falador_tele_confidence))
            pyautogui.keyDown('f2')
            time.sleep(.11 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            pyautogui.keyUp('f2') 
        if time.time() - start_time > 2:
            print('failed to find falador tele. quitting...')
            exit()

    #click falador tele
    falador_tele_screen_point = wincap.get_screen_position(falador_tele_best_point)
    falador_tele_click_point = falador_tele_action.click(falador_tele_screen_point, speed = speed(), wait = wait())
    print('clicked falador_tele | confidence %s' % falador_tele_confidence)
    tick_dropper()
    time.sleep(.15 + abs(np.random.normal(.1,.05)))

    #close magic tab for better vision
    pyautogui.keyDown('f2')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f2')
    print('pressed f2 to close magic tab')

    start_time = time.time()
    last_click_time = time.time()
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        falador_minimap_all_points, falador_minimap_best_point, falador_minimap_confidence = falador_minimap_vision.find(screenshot, threshold = FALADOR_MINIMAP_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()

        print('looking for falador minimap | search time %s | confidence %s ' % (time.time()- start_time, falador_minimap_confidence))

        if falador_minimap_confidence > FALADOR_MINIMAP_THRESHOLD:
            print('found falador minimap | confidence %s' % falador_minimap_confidence)
            break

        if time.time() - last_click_time > (3.5 + abs(np.random.normal(.3,.05))):
            last_click_time = time.time()
            print('looked for %s | no falador minimap found | confidence %s | recalling restock()...' % (time.time() - start_time, falador_minimap_confidence))
            restock()
            return
                  


    #get to the falador bank

    #click minimap
    falador_minimap_screen_point = wincap.get_screen_position(falador_minimap_best_point)
    falador_minimap_click_point = falador_minimap_action.click(falador_minimap_screen_point, speed = speed(), wait=wait())
    print('clicked minimap left side, going to bank | confidence %s' % falador_minimap_confidence)
    tick_dropper()
    #time.sleep(.1 + abs(np.random.normal(.2,.2)))


    #this guy waits around until he sees the bank in the minimap
    print('searching for bank_minimap...')
    bank_minimap_confidence = 0
    start_time = time.time()
    last_click_time = time.time()
    while bank_minimap_confidence < BANK_MINIMAP_THRESHOLD:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_minimap_all_points, bank_minimap_best_point, bank_minimap_confidence = bank_minimap_vision.find(screenshot, threshold = BANK_MINIMAP_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()

        #this is a reclicker. doesn't nessisarily mean a fuckup, sometimes it takes multiple clicks to find the bank
        if (time.time() - last_click_time) > (1.3 + abs(np.random.normal(0,.3))):
            print('search time %s | last click %s | bank_minimap_confidence %s |reclicking minimap left side' % ((time.time() - start_time), (time.time() - last_click_time), bank_minimap_confidence))
            pyautogui.click()
            last_click_time = time.time()
            

        if time.time() - start_time > 12:
            print('search time %s | final confidence %s | unable to find bank_minimap, re-calling restock function' % (time.time() - start_time, bank_minimap_confidence))
            restock() #this move here might give me trouble: if it times out it restarts the restock function. Could loop infinitely
            return

    #we only get here once we've found the bank minimap. now we click
    bank_minimap_screen_point = wincap.get_screen_position(bank_minimap_best_point)
    bank_minimap_click_point = bank_minimap_action.click(bank_minimap_screen_point, speed = speed(), wait=wait())
    print('clicked bank_minimap | confidence %s' % bank_minimap_confidence)
    tick_dropper()


    #this guy waits around until he sees the bank on his screen\
    print('searching for bank...')
    bank_confidence = 0
    start_time = time.time()
    lastclick_time = time.time()
    while bank_confidence < BANK_THRESHOLD:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_all_points, bank_best_point, bank_confidence = bank_vision.find(screenshot, threshold = BANK_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        print('bank search time %s | confidence %s' % (time.time() - start_time, bank_confidence))
        
        if time.time() - last_click_time > 10:
            last_click_time = time.time()
            print('attempting reclick on bank minimap in hopes of finding bank')
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            bank_minimap_all_points, bank_minimap_best_point, bank_minimap_confidence = bank_minimap_vision.find(screenshot, threshold = BANK_MINIMAP_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            bank_minimap_screen_point = wincap.get_screen_position(bank_minimap_best_point)
            bank_minimap_click_point = bank_minimap_action.click(bank_minimap_screen_point, speed = speed(), wait=wait())
            print('re-clicked bank_minimap | confidence %s' % bank_minimap_confidence)
                
        if time.time() - start_time > 30:
            print('bank search time %s | quitting and re-calling restock function...' % (time.time() - start_time))
            restock() #this move here might give me trouble: if it times out it restarts the restock function. Could loop infinitely
            return
    bank_screen_point = wincap.get_screen_position(bank_best_point)
    bank_click_point = bank_action.click(bank_screen_point, speed = .85, wait=wait())
    print('clicked bank | confidence %s' % bank_confidence)

    #we wait until we're in the bank
    in_bank_confidence = 0
    start_time = time.time()
    last_click_time = time.time()
    while in_bank_confidence < IN_BANK_THRESHOLD:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        in_bank_all_points, in_bank_best_point, in_bank_confidence = in_bank_vision.find(screenshot, threshold = IN_BANK_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()  
        print('waiting to be in bank | confidence %s' % in_bank_confidence)

        if time.time() - last_click_time > 3:
            last_click_time = time.time()
            print('not in bank when expected. attempting reclick...')
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            bank_all_points, bank_best_point, bank_confidence = bank_vision.find(screenshot, threshold = BANK_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            bank_screen_point = wincap.get_screen_position(bank_best_point)
            bank_click_point = bank_action.click(bank_screen_point, speed = speed(), wait=wait())
            print('RE-clicked bank | confidence %s' % bank_confidence)


        if time.time() - start_time > 15:
            print('not in bank when expected. reclicks failed. re-calling restock function')
            restock()
            return

    #we click the log
    start_time = time.time()
    last_click_time = time.time()
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_log_all_points, bank_log_best_point, bank_log_confidence = bank_log_vision.find(screenshot, threshold = BANK_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()  
        
        print('bank log search time %s | confidence %s' % (time.time() - start_time, bank_log_confidence))

        if bank_log_confidence > BANK_LOG_THRESHOLD:
            print('clicking bank log | confidence %s' % bank_log_confidence)
            bank_log_screen_point = wincap.get_screen_position(bank_log_best_point)
            bank_log_click_point = bank_log_action.click(bank_log_screen_point)
            break
        
        if time.time() - start_time > 1.5:
            print('failed to find bank log | confidence %s | exiting...' % bank_log_confidence)
            exit()



    #lets see if we got enough logs
    start_time = time.time()
    last_click_time = time.time()
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit() 

        if time.time() - last_click_time > (1.1 + abs(np.random.normal(0,.3))):
            last_click_time = time.time()
            print('log searching for %ss | %s logs found | confidence %s | attempting log reclick' % (time.time() - start_time, len(inv_log_all_points), inv_log_confidence))
            
            #this here is a log reclicker
            reclick_start_time = time.time()
            while True:
                screenshot = wincap.get_screenshot()
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
                bank_log_all_points, bank_log_best_point, bank_log_confidence = bank_log_vision.find(screenshot, threshold = BANK_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    exit()  
                
                print('bank log RE-search time %s | confidence %s' % (time.time() - start_time, bank_log_confidence))

                if bank_log_confidence > BANK_LOG_THRESHOLD:
                    print('RE-clicking bank log | confidence %s' % bank_log_confidence)
                    bank_log_screen_point = wincap.get_screen_position(bank_log_best_point)
                    bank_log_click_point = bank_log_action.click(bank_log_screen_point)
                    break
                
                if time.time() - reclick_start_time > 1.5:
                    print('failed to find bank log for RECLICK | confidence %s | exiting...' % bank_log_confidence)
                    exit()




        if len(inv_log_all_points) < 8:
            print('log searching for %ss | %s logs found | confidence %s | waiting for at least 9' % (time.time() - start_time, len(inv_log_all_points), inv_log_confidence))
        
        
        if len(inv_log_all_points) > 8:
            print('log searched for %ss | %s logs found | confidence %s | exiting bank' %( time.time() - start_time,  len(inv_log_all_points), inv_log_confidence))
            tick_dropper()
            pyautogui.keyDown('esc')
            time.sleep(.15 + abs(np.random.normal(.1,.05)))
            tick_dropper()
            pyautogui.keyUp('esc')
            print('pressed and released esc to exit bank')
            break

        if time.time() - start_time > 5:
            print('failed to find bank log for RECLICK | searched for %s s| confidence %s | exiting...' % (time.time() - start_time, bank_log_confidence))
            exit()

    

def burn_cycle():

    tick_dropper()
    print('starting burn cycle')

    #open magic tab
    pyautogui.keyDown('f2')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f2')
    print('clicked f2 to open magic tab')
    time.sleep(.4 + abs(np.random.normal(.1,.05)))

    global teleport_location

   
    if teleport_location == 'falador':
        #change to next location
        teleport_location = 'lumbridge'
        
        #find falador tele
        start_time = time.time()
        last_click_time = time.time()
        while True:
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            falador_tele_all_points, falador_tele_best_point, falador_tele_confidence = falador_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            print('searching falador_tele for %ss | confidence %s' % (time.time() - start_time, falador_tele_confidence))
            if falador_tele_confidence > TELE_THRESHOLD:
                print('found falador_tele after %ss | confidence %s' % (time.time() - start_time, falador_tele_confidence))
                break
            if time.time() - start_time() > 2:
                print('falador_tele search time %s | giving up and recalling burn_cycle()' % time.time() - start_time)
                burn_cycle()
                return
        
        #click falador tele
        falador_tele_screen_point = wincap.get_screen_position(falador_tele_best_point)
        falador_tele_click_point = falador_tele_action.click(falador_tele_screen_point, speed = speed(), wait = wait())
        print('clicked falador_tele | confidence %s' % falador_tele_confidence)
        tick_dropper()


    elif teleport_location == 'lumbridge':
        #change to next location
        teleport_location = 'varrock'
        
        #find lumbridge tele
        start_time = time.time()
        last_click_time = time.time()
        while True:
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            lumbridge_tele_all_points, lumbridge_tele_best_point, lumbridge_tele_confidence = lumbridge_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            print('searching lumbridge_tele for %ss | confidence %s' % (time.time() - start_time, lumbridge_tele_confidence))
            if lumbridge_tele_confidence > TELE_THRESHOLD:
                print('found lumbridge_tele after %ss | confidence %s' % (time.time() - start_time, lumbridge_tele_confidence))
                break
            if time.time() - start_time() > 2:
                print('lumbridge_tele search time %s | giving up and recalling burn_cycle()' % time.time() - start_time)
                burn_cycle()
                return
        
        #click lumbridge tele
        lumbridge_tele_screen_point = wincap.get_screen_position(lumbridge_tele_best_point)
        lumbridge_tele_click_point = lumbridge_tele_action.click(lumbridge_tele_screen_point, speed = speed(), wait = wait())
        print('clicked lumbridge_tele | confidence %s' % lumbridge_tele_confidence)
        tick_dropper()

    elif teleport_location == 'varrock':
        #change to next location
        teleport_location = 'falador'
        
        #find varrock tele
        start_time = time.time()
        last_click_time = time.time()
        while True:
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            varrock_tele_all_points, varrock_tele_best_point, varrock_tele_confidence = varrock_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            print('searching varrock_tele for %ss | confidence %s' % (time.time() - start_time, varrock_tele_confidence))
            if varrock_tele_confidence > TELE_THRESHOLD:
                print('found varrock_tele after %ss | confidence %s' % (time.time() - start_time, varrock_tele_confidence))
                break
            if time.time() - start_time() > 2:
                print('varrock_tele search time %s | giving up and recalling burn_cycle()' % time.time() - start_time)
                burn_cycle()
                return
        
        #click varrock tele
        varrock_tele_screen_point = wincap.get_screen_position(varrock_tele_best_point)
        varrock_tele_click_point = varrock_tele_action.click(varrock_tele_screen_point, speed = speed(), wait = wait())
        print('clicked varrock_tele | confidence %s' % varrock_tele_confidence)
        tick_dropper()

    time.sleep(.3 + abs(np.random.normal(.1,.2)))

    #open inv
    pyautogui.keyDown('f1')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f1')
    print('clicked f1 to open inv tab')
    time.sleep(.4 + abs(np.random.normal(.1,.05)))
    tick_dropper()


    #find a log
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit() 

    if inv_log_confidence < INV_LOG_THRESHOLD:
        print('no logs, attempting to reopen inv tab')
        pyautogui.keyDown('f1')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        pyautogui.keyUp('f1')
        print('clicked f1 to open inv tab')
        time.sleep(.4 + abs(np.random.normal(.1,.05)))
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit() 

    tick_dropper()
    #click log
    inv_log_screen_point = wincap.get_screen_position(inv_log_best_point)
    inv_log_click_point = inv_log_action.click(inv_log_screen_point, speed = speed(), wait = wait())
    print('clicked log 1/%s | confidence %s' %(len(inv_log_all_points), inv_log_confidence))    
    
    time.sleep(.15 + abs(np.random.normal(.1,.05)))

    #find tidner
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    tinder_all_points, tinder_best_point, tinder_confidence = tinder_vision.find(screenshot, threshold = TINDER_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit() 
    
    #it turns out below is not nessisary, just look for xp drops in color and set the threshold at .999
    '''
    #I do something weird here: i'm taking a base number of firemaking xp drops found, so I can wait for the number to go up by 1 when the real drop comes. The trouble is XP drop is so small that there's no confidence threshold high enough to avoid false positives.
    screenshot = wincap.get_screenshot()        
    firemaking_xp_all_points, firemaking_xp_best_point, firemaking_xp_confidence = firemaking_xp_vision.find(screenshot, threshold = FIREMAKING_XP_THRESHOLD, debug_mode = 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()
    number_false_positives = len(firemaking_xp_all_points)
    '''


    #click tinder
    tick_dropper()
    tinder_screen_point = wincap.get_screen_position(tinder_best_point)
    tinder_click_point = tinder_action.click(tinder_screen_point, speed = speed(), wait = wait())

    print('clicked 1/%s tinder | confidence %s' %(len(tinder_all_points), tinder_confidence))
    

    while len(inv_log_all_points) > 1:
        #find and click on tinder box
        tick_dropper()
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        tinder_all_points, tinder_best_point, tinder_confidence = tinder_vision.find(screenshot, threshold = TINDER_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit() 
        tinder_screen_point = wincap.get_screen_position(tinder_best_point)
        tinder_click_point = tinder_action.click(tinder_screen_point, speed = speed(), wait = wait())
        print('clicked 1/%s tinder | confidence %s' %(len(tinder_all_points), tinder_confidence))
        tick_dropper()

        #find and move cursor to log, but don't click yet
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit() 
        inv_log_screen_point = wincap.get_screen_position(inv_log_best_point)
        inv_log_moveTo_point = inv_log_action.moveTo(inv_log_screen_point, speed = (speed()+.1), wait = wait())
        
        #we're looking now for the firemaking xp drop as a click cue
        start_time = time.time()
        while True:
            screenshot = wincap.get_screenshot()        
            firemaking_xp_all_points, firemaking_xp_best_point, firemaking_xp_confidence = firemaking_xp_vision.find(screenshot, threshold = FIREMAKING_XP_THRESHOLD, debug_mode = 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            
            print('firemaking_xp num %s | confidence %s | search_time %s' % (len(firemaking_xp_all_points), firemaking_xp_confidence, time.time() - start_time ))

            #the xp drop needs to be above confidence threshold, and physically below the blindness border on the screen. 
            #the point of the blindness border to is to hide the second half of the xp drop from the script, creating a period where it cannot see an xp drop. this creates an alternating cycle of drop visible/ no drop visible which can be used to time clicks.
            if firemaking_xp_confidence > FIREMAKING_XP_THRESHOLD and firemaking_xp_best_point[1] > BLINDNESS_BORDER:
                time.sleep(.1 + abs(np.random.normal(0,.08)))
                pyautogui.click()
                print('firemaking_xp spotted at %s | search time %s | Clicking and exiting firemaking_xp search loop' % (firemaking_xp_best_point, time.time() - start_time))
                tick_dropper()
                break

            if time.time() - start_time > (3.5 + abs(np.random.normal(0,.3))):
                print('waited %s, no xp drop | re-calling burn_cycle()' % (time.time()- start_time))
                burn_cycle()
                return
        
        #code below slows it down too much, and the next xp drop is already gone by the time we're back around to seeing it. 
        '''
        #we're waiting to NOT see an xp drop 
        start_time = time.time()
        while True:
            screenshot = wincap.get_screenshot()        
            firemaking_xp_all_points, firemaking_xp_best_point, firemaking_xp_confidence = firemaking_xp_vision.find(screenshot, threshold = FIREMAKING_XP_THRESHOLD, debug_mode = 'rectangles', return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            
            print('firemaking_xp num %s | confidence %s | search_time %s' % (len(firemaking_xp_all_points), firemaking_xp_confidence, time.time() - start_time ))

            #there needs to be no firemaking_xp drop that exceeds the confidence threshold and is physically below the blindness border
            if firemaking_xp_confidence < FIREMAKING_XP_THRESHOLD or firemaking_xp_best_point[1] < BLINDNESS_BORDER:
                print('no firemaking_xp spotted below blindness border | confidence %s | total wait time %s | breaking loop and starting next log burn' % ( firemaking_xp_confidence, time.time() - start_time))
                time.sleep(.05 + abs(np.random.normal(0,.15)))
                tick_dropper()
                break
        '''


        print('clicked 1/%s inv_log | confidence %s ' % (len(inv_log_all_points), inv_log_confidence))
        

        tick_dropper()
       

        tick_dropper()
        old_num_log = len(inv_log_all_points)
        start_time = time.time()
        while old_num_log == len(inv_log_all_points):
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            if time.time() - start_time > .8:
                print('no log change in %s | leaving...' % (time.time() - start_time))
                burn_cycle()
        time.sleep(1 + abs(np.random.normal(0,.2)))
        tick_dropper()
    print(' I now see %s logs | ending burn cycle' % len(inv_log_all_points))    
    return



quit_after_seconds = float(input('please enter the number of seconds to run for, then press enter. 1h = 3600s, 6h = 21600 | '))

print('starting in 5 seconds. CLICK INTO RUNELITE NOW!')
time.sleep(1)
print('4...CLICK INTO RUNELITE NOW!')
time.sleep(1)
print('3...CLICK INTO RUNELITE NOW!')
time.sleep(1)
print('2...CLICK INTO RUNELITE NOW!')
time.sleep(1)
print('1...CLICK INTO RUNELITE NOW!')
time.sleep(1)
print('Now!')

#restock()
burn_cycle()

'''
runStart = time.time()
while True:
    burn_cycle()
    restock()
    if time.time() - runStart > quit_after_seconds:
        print('ran successfully(?) for %ss | quitting...' % (time.time() - runStart))
        exit()

'''