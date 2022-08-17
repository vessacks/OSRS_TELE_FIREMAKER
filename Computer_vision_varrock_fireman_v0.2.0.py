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
#move your tinder box aruond in inventory
#take new in_bank_vision
#take new bank image
#this really only works in resizable modern with a big bank snapshot. 
#tinder box needs to be in top left

#to improve
# you have a bunch of random wait times: you should turn them into wait-for-event times to make it efficient



# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Vessacks')


# initialize the Vision class
inv_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
tinder_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
falador_minimap_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_minimap_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
in_bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\in_bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
varrock_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\varrock_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
falador_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
lumbridge_tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)


#initialize the action class
falador_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele.png')
varrock_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_tele.png')
lumbridge_tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\lumbridge_tele.png')

bank_log_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log.png')

inv_log_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png')
tinder_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png')

falador_minimap_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap_mask.png',0)
falador_minimap_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\falador_minimap.png', mask= falador_minimap_mask, face_size= [48,93])

bank_minimap_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap_mask.png',0)
bank_minimap_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap.png', mask= bank_minimap_mask, face_size= [29,29]) #note: i'm eyeballing this size. take a look if it causes problems

bank_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_mask.png',0)
bank_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_minimap.png', mask= bank_mask, face_size= [66,20]) #note: with a zone this small, there may be no room to walk



#constants
RUNE_THRESHOLD = .85
TELE_THRESHOLD = .92
FALADOR_MINIMAP_THRESHOLD = .8
BANK_MINIMAP_THRESHOLD =.7
BANK_THRESHOLD = .57
IN_BANK_THRESHOLD =.85
BANK_LOG_THRESHOLD = .80
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


#this function takes you to falador bank and restocks
def restock():
    time.sleep(1) #need this for complicated reasons. basically it can fuck up reclicks if you dont' wait


    #open magic tab
    time.sleep(wait())
    tick_dropper()


    pyautogui.keyDown('f2')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f2')
    print('clicked f2 to open magic menu')
    time.sleep(.4 + abs(np.random.normal(.1,.05)))


    #find falador tele
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    falador_tele_all_points, falador_tele_best_point, falador_tele_confidence = falador_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()
    time.sleep(wait())
    tick_dropper()

    #click falador tele
    falador_tele_screen_point = wincap.get_screen_position(falador_tele_best_point)
    falador_tele_click_point = falador_tele_action.click(falador_tele_screen_point, speed = speed(), wait = wait())
    print('clicked falador_tele | confidence %s' % falador_tele_confidence)
    
    
    time.sleep(3.5 + abs(np.random.normal(.3,.05)))

    #get to the falador bank


    #find the minimap
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    falador_minimap_all_points, falador_minimap_best_point, falador_minimap_confidence = falador_minimap_vision.find(screenshot, threshold = FALADOR_MINIMAP_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()

    #click minimap
    falador_minimap_screen_point = wincap.get_screen_position(falador_minimap_best_point)
    falador_minimap_click_point = falador_minimap_action.click(falador_minimap_screen_point, speed = speed(), wait=wait())
    print('clicked minimap left side, going to bank | confidence %s' % falador_minimap_confidence)
    time.sleep(.1 + abs(np.random.normal(.2,.2)))


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
    
    #we only get here once we've found the bank minimap. now we click
    bank_minimap_screen_point = wincap.get_screen_position(bank_minimap_best_point)
    bank_minimap_click_point = bank_minimap_action.click(bank_minimap_screen_point, speed = speed(), wait=wait())
    print('clicked bank_minimap | confidence %s' % bank_minimap_confidence)


    #close magic tab for better vision
    pyautogui.keyDown('f2')
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp('f2')
    print('clicked f2 to close magic tab')


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
    
    bank_screen_point = wincap.get_screen_position(bank_best_point)
    bank_click_point = bank_action.click(bank_screen_point, speed = speed(), wait=wait())
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
        

    #we click the log
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    bank_log_all_points, bank_log_best_point, bank_log_confidence = bank_log_vision.find(screenshot, threshold = BANK_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()  

    if bank_log_confidence > BANK_LOG_THRESHOLD:
        print('clicking bank log | confidence %s' % bank_log_confidence)
        bank_log_screen_point = wincap.get_screen_position(bank_log_best_point)
        bank_log_click_point = bank_log_action.click(bank_log_screen_point)
    else: 
        print('bank log confidence %s | too low, attempting re-call of restock...' % bank_log_confidence)
        restock()
    
    time.sleep(.4 + abs(np.random.normal(0,.3)))

    #lets see if we got enough logs
    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit() 


    if len(inv_log_all_points) > 8:
        print('I see %s logs, exiting bank' % len(inv_log_all_points))
        pyautogui.keyDown('esc')
        time.sleep(.15 + abs(np.random.normal(.1,.05)))
        tick_dropper()
        pyautogui.keyUp('esc')
    
    else: 
        print(' not enough logs (%s), re-calling restock...' % len(inv_log_all_points))
        restock()

    return
    

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

    locations = ['falador', 'lumbridge', 'varrock']

    teleport_location = locations[np.random.randint(0,3)]

    if teleport_location == 'falador':
        #find falador tele
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        falador_tele_all_points, falador_tele_best_point, falador_tele_confidence = falador_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        time.sleep(wait())
        tick_dropper()

        #click falador tele
        falador_tele_screen_point = wincap.get_screen_position(falador_tele_best_point)
        falador_tele_click_point = falador_tele_action.click(falador_tele_screen_point, speed = speed(), wait = wait())
        print('clicked falador_tele | confidence %s' % falador_tele_confidence)


    elif teleport_location == 'lumbridge':
        #find lumbridge tele
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        lumbridge_tele_all_points, lumbridge_tele_best_point, lumbridge_tele_confidence = lumbridge_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        time.sleep(wait())
        tick_dropper()

        #click lumbridge tele
        lumbridge_tele_screen_point = wincap.get_screen_position(lumbridge_tele_best_point)
        lumbridge_tele_click_point = lumbridge_tele_action.click(lumbridge_tele_screen_point, speed = speed(), wait = wait())
        print('clicked lumbridge_tele | confidence %s' % lumbridge_tele_confidence)

    elif teleport_location == 'varrock':
        #find varrock tele
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        varrock_tele_all_points, varrock_tele_best_point, varrock_tele_confidence = varrock_tele_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        time.sleep(wait())
        tick_dropper()

        #click varrock tele
        varrock_tele_screen_point = wincap.get_screen_position(varrock_tele_best_point)
        varrock_tele_click_point = varrock_tele_action.click(varrock_tele_screen_point, speed = speed(), wait = wait())
        print('clicked varrock_tele | confidence %s' % varrock_tele_confidence)

    time.sleep(3.5 + abs(np.random.normal(.3,.2)))

    #open inv
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

    inv_log_screen_point = wincap.get_screen_position(inv_log_best_point)
    inv_log_click_point = inv_log_action.click(inv_log_screen_point, speed = speed(), wait = wait())

    print('clicked log 1/%s | confidence %s' %(len(inv_log_all_points), inv_log_confidence))    

    screenshot = wincap.get_screenshot()
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    tinder_all_points, tinder_best_point, tinder_confidence = tinder_vision.find(screenshot, threshold = TINDER_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit() 
    tinder_screen_point = wincap.get_screen_position(tinder_best_point)
    tinder_click_point = tinder_action.click(tinder_screen_point, speed = speed(), wait = wait())

    print('clicked 1/%s tinder | confidence %s' %(len(tinder_all_points), tinder_confidence))
    
    time.sleep(2.3 + abs(np.random.normal(0,.3)))

    while len(inv_log_all_points) > 1:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        inv_log_all_points, inv_log_best_point, inv_log_confidence = inv_log_vision.find(screenshot, threshold = INV_LOG_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit() 
        inv_log_screen_point = wincap.get_screen_position(inv_log_best_point)
        inv_log_click_point = inv_log_action.click(inv_log_screen_point, speed = speed(), wait = wait())
        print('clicked 1/%s inv_log | confidence %s ' % (len(inv_log_all_points), inv_log_confidence))
        

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


runStart = time.time()
count = 0

while True:
    burn_cycle()
    restock()
    if time.time() - runStart > quit_after_seconds:
        print('ran successfully(?) for %ss | quitting...' % (time.time() - runStart))
        exit()

