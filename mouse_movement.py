from pyautogui import *
import win32api, win32gui, win32con
import keyboard
import time

class Mouse():
    activated = False
    speed = 2

    def move(self, direction):
        flags, hcursor, (x,y) = win32gui.GetCursorInfo()
        if direction == 'up':
            y-=self.speed
        if direction == 'down':
            y+=self.speed
        if direction == 'left':
            x-=self.speed
        if direction == 'right':
            x+=self.speed
        win32api.SetCursorPos((x,y))

    def click(self, side):
        if side == 'ctrl':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        if side == 'alt':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

#Main program
m1 = Mouse()
key = ('up','down','left','right')
click= ('shift', 'ctrl')

while not keyboard.is_pressed('ctrl+.'):
    
    if keyboard.is_pressed('ctrl+alt'):
        m1.activated = not m1.activated
        print('keyboard script is: '+ str(m1.activated))
        time.sleep(0.5)

    if m1.activated:
        for x in key:
            if keyboard.is_pressed(x):
                m1.move(x)
        for x in click:
            if keyboard.is_pressed(x):
                m1.click(x)
        time.sleep(0.002)


