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

# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Vessacks')


# initialize the Vision class
inv_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
tinder_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinderbox.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
center_minimap_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\center_minimap.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
in_bank_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
bank_log_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank_log.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
tele_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tele.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
north_tile_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\north_tile.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)
south_tile_vision = Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\south_tile.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_GRAYSCALE)



#initialize the action class
tele_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tele.png')
inv_log_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\inv_log.png')
tinder_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tinder.png')
center_minimap_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\tele.png')
bank_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\bank.png')
north_tile_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\north_tile.png')
south_tile_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\Varrock Firemaker\\image library\\south_tile.png')



#constants
RUNE_THRESHOLD = .85
TELE_THRESHOLD = .92
SOUTH_TILE_THRESHOLD =.6

south_tile_cycle = True

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
    wait = (.1 + abs(np.random.uniform(0,.05)))
    return wait


while True:
    #open magic menu
    pyautogui.keyDown('f6')
    time.sleep(.1 + abs(np.random.normal(0,.05)))
    
    #varrock tele
    print('looking for tele')
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        tele_all_points, tele_best_point, tele_confidence = bank_vision.find(screenshot, threshold = TELE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        if tele_confidence > TELE_THRESHOLD:
            print('found tele')
            break
    tele_screen_point = wincap.get_screen_position(tele_best_point)
    tele_click_point = tele_action.click(tele_screen_point, speed = speed(), wait = wait())
    print('clicked tele')

    #click south_tile
    print('looking for south_tile')
    while True:
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        south_tile_all_points, south_tile_best_point, south_tile_confidence = bank_vision.find(screenshot, threshold = SOUTH_TILE_THRESHOLD, return_mode= 'allPoints + bestPoint + confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        if south_tile_confidence > SOUTH_TILE_THRESHOLD:
            print('found south_tile')
            break
    south_tile_screen_point = wincap.get_screen_position(south_tile_best_point)
    south_tile_click_point = south_tile_action.click(south_tile_screen_point, speed = speed(), wait = wait())
    print('clicked south_tile')

    #wait to get to south tile. this is a guessing game, and the number may have to be tweaked
    time.sleep(4 + np.random.normal(0,.3))

    #determine if it is a south tile run or north tile run
    if south_tile_cycle == True:
        print('south_tile_cycle == True, setting to False')
        south_tile_cycle = False
    elif south_tile_cycle == False:
        print('south_tile_cycle == False, setting to True')
        south_tile_cycle = True
    else: 
        print('south_tile_cycle neither true nor false, fuckup detected. Exiting...')
        exit()
    
    


    





#everything below this is scraps for use in program





WITHDRAW_18_OFFSET = [-117,64] #these are the coord offsets between a righclick point and the withdraw 18 dropdown option



def wait():
    wait = (.06 + abs(np.random.uniform(0,.02)))
    return wait

def speed():
    speed = np.random.normal(.78,.3)
    while speed > .85 or speed < .6:
        speed = np.random.normal(.75,.08)
    return speed

def tick_dropper(odds=100):
    if np.random.randint(0,odds) == 1:
        time.sleep(.6)


s_or_c = input('would you like to run in seconds or counts? please enter \'s\' or \'c\'')

if s_or_c == 's':
    quit_after_seconds = float(input('please enter the number of seconds to run for, then press enter. 1h = 3600s, 6h = 21600'))
if s_or_c == 'c':
    quit_after_counts = int(input('please enter the number of counts to run for, then press enter. about 8s per count.'))
else:
    print('you\'ve screwed something up. try running this program again. exiting...')
    exit()

runStart = time.time()
count = 0

def superglass_make():    
    while True:

        #waiting a bit for spell to cast
        sleepytime = 1.8 + abs(np.random.normal(0,.1))
        time.sleep(sleepytime)        

        #below is the old way of entering the bank and finding bank dump. to return to this method, change sleepytime action (first thing in loop) to 1.8 seconds,and delete everything between sleepytime and this comment
        
        #enter bank
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_confidence = bank_vision.find(screenshot, threshold = BANK_THRESHOLD, return_mode= 'confidence')
        if bank_confidence[1] < BANK_THRESHOLD:
            print(' PROBLEM(!) bank confidence %s | BANK_THRESHOLD %s | Continuing anyway...' %( bank_confidence[1], BANK_THRESHOLD))
            #exit()
        else:
            print('bank confidence %s | BANK_THRESHOLD %s | Continuing...' %( bank_confidence[1], BANK_THRESHOLD))
        bank_screenPoint = wincap.get_screen_position(bank_confidence[0])
        bank_clickPoint = bank_action.click(bank_screenPoint, speed = speed(), wait = wait())
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        
        #look for bank dump: this takes a variable amount of time
        bank_dump_confidence = [[0,0],0]
        search_start = time.time()
        search_time = 0
        while bank_dump_confidence[1] < BANK_DUMP_THRESHOLD:
            screenshot = wincap.get_screenshot()
            screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
            bank_dump_confidence = bank_dump_vision.find(screenshot, threshold = BANK_DUMP_THRESHOLD, return_mode= 'confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()

            search_time = time.time() - search_start
            if search_time > 2:
                screenshot = wincap.get_screenshot()
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
                bank_confidence = bank_vision.find(screenshot, threshold = BANK_THRESHOLD, return_mode= 'confidence')
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    exit()
                if bank_confidence[1] < BANK_THRESHOLD_RECLICK:
                    print('2+ seconds since bank click. PROBLEM(!) bank confidence %s below BANK_THRESHOLD DISABLED(!) %s | continuing anyway...' %( bank_confidence[1], BANK_THRESHOLD))
                    exit()
                else:
                    print('2+ seoncds inactivity. attempting reclick on bank and sleeping ~.6s. bank confidence %s | BANK_THRESHOLD DISABLED(!) %s | Continuing...' %( bank_confidence[1], BANK_THRESHOLD))
                bank_screenPoint = wincap.get_screen_position(bank_confidence[0])
                bank_clickPoint = bank_action.click(bank_screenPoint, speed = speed(),wait = wait())
                #wait to get to bank
                time.sleep(.3 + abs(np.random.normal(0,.3)))
                #check if recovery worked
                screenshot = wincap.get_screenshot()
                screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
                bank_dump_confidence = bank_dump_vision.find(screenshot, threshold = BANK_DUMP_THRESHOLD, return_mode= 'confidence')
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    exit()
                if bank_dump_confidence[1] > BANK_DUMP_THRESHOLD:
                    print('in_bank confidence = %s. reclick worked, continuing...' % bank_dump_confidence[1])
                    break


            if search_time > 20:
                print('PROBLEM(!) 20s+ inactivity. multiple reclicks failed. giving up, exitting...')
                exit()
        

        #this code should be redundant but I'm leaving it in anyway for debugging
        
        if bank_dump_confidence[1] < BANK_DUMP_THRESHOLD:
            print('bank_dump_confidence %s | BANK_DUMP_THRESHOLD %s | Exiting...' %( bank_dump_confidence[1], BANK_DUMP_THRESHOLD))
            exit()
        else:
            print('bank_dump_confidence %s | BANK_DUMP_THRESHOLD %s | Continuing...' %( bank_dump_confidence[1], BANK_DUMP_THRESHOLD))
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_dump_confidence = bank_dump_vision.find(screenshot, threshold = BANK_DUMP_THRESHOLD, return_mode= 'confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        bank_dump_screenPoint = wincap.get_screen_position(bank_dump_confidence[0])
        bank_dump_clickPoint = bank_dump_action.click(bank_dump_screenPoint, speed = speed(),wait = wait())

        tick_dropper()

        #take two rune
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        rune_confidence = rune_vision.find(screenshot, threshold = RUNE_THRESHOLD, debug_mode= 'rectangles', return_mode= 'confidence')
        if rune_confidence[1] < RUNE_THRESHOLD:
            print('rune confidence %s | RUNE_THRESHOLD %s | Exiting...' %( rune_confidence[1], RUNE_THRESHOLD))
            exit()
        else:
            print('rune confidence %s | RUNE_THRESHOLD %s | Continuing...' %( rune_confidence[1], RUNE_THRESHOLD))
        rune_screenPoint = wincap.get_screen_position(rune_confidence[0])
        rune_clickPoint = rune_action.click(rune_screenPoint, speed = speed(),wait = wait())
        time.sleep(abs(np.random.normal(.14,.01)))
        pyautogui.click()  
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()
        
        
        tick_dropper()


        #take three weed
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        weed_confidence = weed_vision.find(screenshot, threshold = WEED_THRESHOLD, debug_mode= 'rectangles', return_mode= 'confidence')
        if weed_confidence[1] < WEED_THRESHOLD:
            print('weed confidence %s | WEED_THRESHOLD %s | Exiting...' %( weed_confidence[1], WEED_THRESHOLD))
            exit()
        else:
            print('weed confidence %s | WEED_THRESHOLD %s | Continuing...' %( weed_confidence[1], WEED_THRESHOLD))
        weed_screenPoint = wincap.get_screen_position(weed_confidence[0])
        weed_clickPoint = weed_action.click(weed_screenPoint, speed = speed(), wait = wait())
        time.sleep(abs(np.random.normal(.14,.01)))
        pyautogui.click()  
        time.sleep(abs(np.random.normal(.14,.01)))
        pyautogui.click() 
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()    

        tick_dropper()

        #right click sand
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        sand_confidence = sand_vision.find(screenshot, threshold = SAND_THRESHOLD, debug_mode= 'rectangles', return_mode= 'confidence')
        if sand_confidence[1] < SAND_THRESHOLD:
            print('sand confidence %s | SAND_THRESHOLD %s | Exiting...' %( sand_confidence[1], SAND_THRESHOLD))
            exit()
        else:
            print('sand confidence %s | SAND_THRESHOLD %s | Continuing...' %( sand_confidence[1], SAND_THRESHOLD))
        sand_screenPoint = wincap.get_screen_position(sand_confidence[0])
        sand_clickPoint = sand_action.rightClick(sand_screenPoint, speed = speed())
        if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()    

        sleepytime = abs(np.random.normal(0,.05))
        time.sleep(sleepytime)

        #click withdraw 18
        withdraw_18_screenPoint = [sand_clickPoint[0]+WITHDRAW_18_OFFSET[0], sand_clickPoint[1]+WITHDRAW_18_OFFSET[1]]
        withdraw_18_clickPoint = withdraw_18_action.click(withdraw_18_screenPoint, speed = speed(), wait = wait())

        tick_dropper()

        #exit the bank
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        bank_x_confidence = bank_x_vision.find(screenshot, threshold = BANK_X_THRESHOLD, debug_mode= 'rectangles', return_mode= 'confidence')
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()        

        if bank_x_confidence[1] < BANK_X_THRESHOLD:
            print('bank_x confidence %s | BANK_X_THRESHOLD %s | Exiting...' %( bank_x_confidence[1], BANK_X_THRESHOLD))
            #exit()
        else:
            print('bank_x confidence %s | BANK_X_THRESHOLD %s | Continuing...' %( bank_x_confidence[1], BANK_X_THRESHOLD))
        bank_x_screenPoint = wincap.get_screen_position(bank_x_confidence[0])
        bank_x_clickPoint = bank_x_action.click(bank_x_screenPoint, speed = speed(), wait = wait())
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()        

        sleepytime = .15 + abs(np.random.normal(0,.05))
        time.sleep(sleepytime)

        #cast spell
        screenshot = wincap.get_screenshot()
        screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
        spellcast_confidence = spellcast_vision.find(screenshot, threshold = SPELLCAST_THRESHOLD, debug_mode= 'rectangles', return_mode= 'confidence')
        if spellcast_confidence[1] < SPELLCAST_THRESHOLD:
            print('spellcast confidence %s | SPELLCAST_THRESHOLD %s | exitting...' %( spellcast_confidence[1], SPELLCAST_THRESHOLD))
            exit()
        else:
            print('spellcast confidence %s | SPELLCAST_THRESHOLD %s | Continuing...' %( spellcast_confidence[1], SPELLCAST_THRESHOLD))
        spellcast_screenPoint = wincap.get_screen_position(spellcast_confidence[0])
        spellcast_clickPoint = spellcast_action.click(spellcast_screenPoint, speed = speed(), wait = wait())
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            exit()        





        #debuggery below
        if s_or_c == 's':
            runTime = time.time() - runStart
            if runTime >= quit_after_seconds:
                print('finished after running for %s seconds' % runTime)
                exit()
            print('runtime = %s | seconds remaining = %s' %(runTime, (quit_after_seconds - runTime)))
        if s_or_c == 'c':
            global count
            count = count + 1
            if count >= quit_after_counts:
                print('finished after running %s counts. exitting.. ' % count)
                exit()
            print('count = %s | counts remaining %s' % (count, (quit_after_counts - count)))

while True:
    superglass_make()
    breakRoller.breakRoller(odds = 300, minseconds = 60, maxseconds = 200)
