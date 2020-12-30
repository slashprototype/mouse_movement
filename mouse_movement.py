from pyautogui import *
import win32api, win32gui, win32con
import keyboard
import time

class Mouse():
    activated = False
    speed = 3
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
        if side == "left":
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Main program
m1 = Mouse()
key = ('up','down','left','right')

while not keyboard.is_pressed('ctrl+shift'):
    
    if keyboard.is_pressed('ctrl+alt'):
        m1.activated=   not m1.activated
        print(m1.activated)
        time.sleep(0.5)




    if m1.activated:
        if keyboard.is_pressed('up'):
            m1.move('up')
        if keyboard.is_pressed('down'):
            m1.move('down')
        if keyboard.is_pressed('left'):
            m1.move('left')
        if keyboard.is_pressed('right'):
            m1.move('right')
        if keyboard.is_pressed('shift'):
            m1.click('left')
        time.sleep(0.01)

 