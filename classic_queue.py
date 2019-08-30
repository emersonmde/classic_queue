#! python

import pyautogui
import time
import random
import os
import sys

def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

def findLocation():
    pass
    screen = pyautogui.screenshot()
    realmSelect = pyautogui.locate(resourcePath('images/realm_selection.png'), screen, grayscale=True, confidence=.9)
    changeRealm = pyautogui.locate(resourcePath('images/change_realm.png'), screen, grayscale=True, confidence=.9)
    enterWorld = pyautogui.locate(resourcePath('images/enter_world.png'), screen, grayscale=True, confidence=.9)

    if realmSelect is not None:
        return 'REALM_SELECT'
    elif changeRealm is not None:
        return 'CHANGE_REALM'
    elif enterWorld is not None:
        return 'ENTER_REALM'
    else:
        return 'IN_GAME'

# Give enough time to open wow
time.sleep(30)
while True:
    location = findLocation()

    if location == 'REALM_SELECT':
        # We're on the realm selection screen
        # Click the correct server and then click okay
        print('Selecting realm...')
        server = pyautogui.locateOnScreen(resourcePath('server.png'), grayscale=True, confidence=.9)
        if server is None:
            time.sleep(2)
            continue

        serverPoint = pyautogui.center(server)
        pyautogui.moveTo(serverPoint.x, serverPoint.y, .75)
        pyautogui.click()

        realmSelectOkay = pyautogui.locateOnScreen(resourcePath('images/realm_selection_okay.png'), grayscale=True, confidence=.9)
        if realmSelectOkay is None:
            time.sleep(2)
            continue
        
        realmSelectOkayPoint = pyautogui.center(realmSelectOkay)
        pyautogui.moveTo(realmSelectOkayPoint.x, realmSelectOkayPoint.y, .75)
        pyautogui.click()

        time.sleep(10)
    elif location == 'CHANGE_REALM':
        # Welcome to the queue.. /afk
        print('Waiting in queue - moving mouse')
        windowSize = pyautogui.size()
        x1 = windowSize.width / 2
        y1 = windowSize.height / 2
        x1 = x1 - random.randrange(2, 50)
        y1 = y1 - random.randrange(2, 50)

        x2 = x1 + random.randrange(2, 50)
        y2 = y1 + random.randrange(2, 50)

        pyautogui.moveTo(x1, y1, 1)
        pyautogui.moveTo(x2, y2, 1)
        time.sleep(30)
    elif location == 'ENTER_REALM':
        print('Submitting inputs on the character selection screen')
        # Made it to character selection
        # Randomly hit left/right and add some mouse drags

        # time.sleep(5)
        # enterRealm = pyautogui.locateOnScreen('images/enter_world.png', grayscale=True, confidence=.9)
        # if enterRealm is None:
        #     time.sleep(2)
        #     continue

        # enterRealmPoint = pyautogui.center(enterRealm)
        # pyautogui.moveTo(enterRealmPoint.x, enterRealmPoint.y, .75)
        # pyautogui.click()

        keys = ['left', 'right']
        keyChoice = random.choice(keys)
        pyautogui.press(keyChoice)

        time.sleep(random.randrange(1, 30))

        # Add some mouse drags for good measure
        windowSize = pyautogui.size()
        x1 = windowSize.width / 2
        y1 = windowSize.height / 2
        x1 = x1 - random.randrange(2, 50)
        y1 = y1 - random.randrange(2, 50)

        x2 = x1 + random.randrange(2, 50)
        y2 = y1 + random.randrange(2, 50)

        pyautogui.moveTo(x1, y1, 1)
        pyautogui.dragTo(x2, y2, duration=random.randrange(1, 3), button='left')

        time.sleep(random.randrange(1, 30))
    else:
        # Not sure where we are, wait and hope we end up somehwere better
        print('Not in game')
        time.sleep(30)
        pass


