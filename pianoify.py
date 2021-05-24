import pyautogui
import pygame.midi
import time
import asyncio
import win32api, win32con


def readInput(input_device):
    if input_device.poll():
        event = input_device.read(1)[0]
        data = event[0]
        timestamp = event[1]
        note_number = data[1]
        velocity = data[2]
        if velocity != 64:
            return note_number

def performAction(key):
    if key == 74: ## c but an octave above middle c
        pyautogui.keyDown("a")
        time.sleep(0.5)
        pyautogui.keyUp("a")
    elif key == 77: ## f but an octave above middle c
        pyautogui.keyDown("d")
        time.sleep(0.5)
        pyautogui.keyUp("d")
    elif key == 72: ## e but an octave above middle c
        pyautogui.keyDown("w")
        time.sleep(0.5)
        pyautogui.keyUp("w")
    elif key == 76: ## d but an octave above middle c
        pyautogui.keyDown("s")
        time.sleep(0.5)
        pyautogui.keyUp("s")
    
    elif key == 60:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -75, 0, 0, 0)

    elif key == 61:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -75, 0, 0)

    elif key == 62:
        pyautogui.leftClick()
    
    elif key == 63:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 75, 0, 0)

    elif key == 64:
        pyautogui.rightClick()

    elif key == 65:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 75, 0, 0, 0)
    
    #if key != None:
    #    print(key)


if __name__ == '__main__':
    pygame.midi.init()
    my_input = pygame.midi.Input(1) #only in my case the id is 2
    while True:
        performAction(readInput(my_input))