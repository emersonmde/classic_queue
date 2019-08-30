#! python

import pyautogui
import time
import random

def findLocation():
    pass
    screen = pyautogui.screenshot()
    realmSelect = pyautogui.locate('images/realm_selection.png', screen, grayscale=True, confidence=.9)
    changeRealm = pyautogui.locate('images/change_realm.png', screen, grayscale=True, confidence=.9)
    enterWorld = pyautogui.locate('images/enter_world.png', screen, grayscale=True, confidence=.9)

    if realmSelect is not None:
        return 'REALM_SELECT'
    elif changeRealm is not None:
        return 'CHANGE_REALM'
    elif enterWorld is not None:
        return 'ENTER_REALM'
    else:
        return 'IN_GAME'

while True:
    location = findLocation()

    if location == 'REALM_SELECT':
        server = pyautogui.locateOnScreen('server.png', grayscale=True, confidence=.9)
        if server is None:
            time.sleep(2)
            continue

        serverPoint = pyautogui.center(server)
        pyautogui.moveTo(serverPoint.x, serverPoint.y, .75)
        pyautogui.click()

        realmSelectOkay = pyautogui.locateOnScreen('images/realm_selection_okay.png', grayscale=True, confidence=.9)
        if realmSelectOkay is None:
            time.sleep(2)
            continue
        
        realmSelectOkayPoint = pyautogui.center(realmSelectOkay)
        pyautogui.moveTo(realmSelectOkayPoint.x, realmSelectOkayPoint.y, .75)
        pyautogui.click()

        #time.sleep(10)
        time.sleep(5)

    elif location == 'CHANGE_REALM':
        #time.sleep(5)
        time.sleep(60)
    elif location == 'ENTER_REALM':
        #time.sleep(30)
        time.sleep(5)
        enterRealm = pyautogui.locateOnScreen('images/enter_world.png', grayscale=True, confidence=.9)
        if enterRealm is None:
            time.sleep(2)
            continue

        enterRealmPoint = pyautogui.center(enterRealm)
        pyautogui.moveTo(enterRealmPoint.x, enterRealmPoint.y, .75)
        pyautogui.click()

    else:
        keys = ['left', 'right', 'space']
        keyChoice = random.choice(keys)
        pyautogui.press(keyChoice)

        #time.sleep(random.randrange(5, 30))
        time.sleep(random.randrange(1, 3))

        # Add some mouse drags for good measure
        windowSize = pyautogui.size()
        x1 = windowSize.width / 2
        y1 = windowSize.height / 2
        x1 = x1 - random.randrange(2, 50)
        y1 = y1 - random.randrange(2, 50)

        x2 = x1 + random.randrange(2, 50)
        y2 = y1 + random.randrange(2, 50)

        pyautogui.moveTo(x1, y1, 1)
        pyautogui.dragTo(x2, y2, duration=random.randrange(1, 3), button='right')

        #time.sleep(5)


