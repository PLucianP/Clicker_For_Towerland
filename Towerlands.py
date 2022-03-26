import pyautogui
from time import sleep
import os

os.getcwd()
os.chdir('Images')
path = os.getcwd()
sleep(2)


def click(var):
    x, y = pyautogui.center(var)
    pyautogui.click(x, y)
    sleep(0.05)


try:
    while True:
        # Target buttons
        Battle = pyautogui.locateOnScreen('{}\\Battle.png'.format(path), grayscale=True, confidence=0.8)
        BattleBoss = pyautogui.locateOnScreen('{}\\BattleBoss.png'.format(path), grayscale=True, confidence=0.8)
        Cont = pyautogui.locateOnScreen('{}\\Continue.png'.format(path), grayscale=True, confidence=0.8)
        Close = pyautogui.locateOnScreen('{}\\Close.png'.format(path), grayscale=True, confidence=0.8)
        # Find the area of where the skills are
        Skill_Archer = pyautogui.locateOnScreen('{}\\Skill_Archer.png'.format(path), region=(170, 300, 420, 680),
                                                grayscale=True, confidence=0.8)
        # Click on Battle, Continue and Exit
        if Battle is not None:
            click(Battle)
        elif BattleBoss is not None:
            click(BattleBoss)
        elif Cont is not None:
            click(Cont)
        elif Close is not None:
            click(Close)
        # Click the skills
        elif Skill_Archer is not None:
            click(Skill_Archer)
            pyautogui.click(1650, 850)

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass
