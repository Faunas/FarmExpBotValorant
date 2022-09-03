import pyautogui
from time import sleep
import mouse
from notifiers import get_notifier
import keyboard
import telegram_send
end_counter = 0
chat_ID1 = 1227493429
import random
from random import randint
telegram = get_notifier('telegram')
messages = 'Игра завершена. Начинаю поиск новой игры..'
def shoot():
    for i in range(25):
        proverka()
        mouse.double_click(button='left')
        sleep(1)
        randomaction()
        start_again()
def start_again():
    mouse.move("921", "1009")
    pyautogui.moveTo(921, 1009)
    mouse.double_click(button='left')
def proverka():
    if pyautogui.locateOnScreen('PlayAgain.png'):
        telegram.notify(message=messages, token='5103076975:AAHkT_5T2CnyK0vWREMgFAqnXP22Vdm-w0U', chat_id=chat_ID1)
        print(pyautogui.locateOnScreen('PlayAgain.png'))
        start_again()
        pyautogui.screenshot('gameend' + str(random.randint(0,10000000))+ '.png')
def randomaction():
    #  proverka()
    n2 = randint(1, 8)
    print(n2)
    if n2 == 1:
        pyautogui.keyDown('w')
        sleep(randint(2, 6) / 10)
    if n2 == 2:
        pyautogui.keyUp('w')
        pyautogui.keyDown('d')
        pyautogui.click()
    if n2 == 3:
        pyautogui.keyDown('a')
        sleep(randint(1, 3) / 10)
        pyautogui.keyDown('a')
        pyautogui.click()
        sleep(randint(2, 4) / 10)
    if n2 == 4:
        pyautogui.keyUp('d')
        pyautogui.keyDown('s')
        sleep(randint(2, 5) / 10)
    if n2 == 5:
        pyautogui.keyUp('s')
        sleep(randint(4, 6) / 10)
    if n2 == 6:
        pyautogui.keyDown('w')
        sleep(randint(2, 4) / 10)
        pyautogui.keyUp('w')
    if n2 == 7:
        pyautogui.keyDown('3')
        sleep(randint(2, 4) / 100)
        pyautogui.keyUp('3')
        sleep(randint(20, 40) / 100)
        pyautogui.keyDown('1')
        sleep(randint(2, 4) / 100)
        pyautogui.keyUp('1')
    if n2 == 8:
        pyautogui.mouseDown(button='left')
        sleep(randint(2, 4))
        pyautogui.mouseUp(button='left')
    proverka()