from time import sleep
import keyboard
import numpy as np
import ctypes
import win32api, win32con
import threading
import mss

def click(x,y):
    win32api.SetCursorPos((x,y))
    sleep(0.04)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
hdc = ctypes.windll.user32.GetDC(0)
que = []
sct = mss.mss()
def presskey(key):
    keyboard.press(key)
    sleep(0.05)
    keyboard.release(key)
def line(x,y,offset,key):
    while True:
        if keyboard.is_pressed("q"):
            break
        color = np.array(sct.grab({"top":y,"left":x,"width":1,"height":1}))
        #color = ctypes.windll.gdi32.GetPixel(hdc, x, y+offset)
        #color2 = ctypes.windll.gdi32.GetPixel(hdc, x, y+offset+5)
        #color3 = ctypes.windll.gdi32.GetPixel(hdc, x, y+offset+5)
        #print(threading.current_thread().name + str(np.sum(color[0][0][:3])))
        if int(color[0][0][0]) < 109:
        #if (color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 330:
            '''(color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 100
            win32api.SetCursorPos((x,y))
            sleep(0.04)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            print(str(threading.currentThread().name)+" clicking "+str((color % 256)+((color // 256) % 256)+(color // (256 ** 2))))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            '''
            #que.append((x,y+80+offset))
            #click(x,y+60+offset
            keyboard.press_and_release(key)
            #threading.Thread(target=presskey,args=(key)).start()
            sleep(0.1)
            #print(key)
qy=620
sleep(1)
print("Program started")
threading.Thread(target=line,name="Th-1",args=(666,qy,0,'g'),daemon=True).start()
threading.Thread(target=line,name="Th-2",args=(810,qy,0,'h'),daemon=True).start()
threading.Thread(target=line,name="Th-3",args=(950,qy,0,'j'),daemon=True).start()
threading.Thread(target=line,name="Th-4",args=(1090,qy,0,'k'),daemon=True).start()

while True:
    if keyboard.is_pressed("q"):
        break
    #if len(que)>0:
        #x,y=que.pop(0)
        #click(x,y)
    '''
    color = ctypes.windll.gdi32.GetPixel(hdc, 780, 750)
    print((color % 256)+((color // 256) % 256)+(color // (256 ** 2)),end=" ")
    if (color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 100:
        click(780,750)
    color = ctypes.windll.gdi32.GetPixel(hdc, 900, 750) 
    print((color % 256)+((color // 256) % 256)+(color // (256 ** 2)),end=" ")
    if (color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 100:
        click(900,750)
    color = ctypes.windll.gdi32.GetPixel(hdc, 1020, 750) 
    print((color % 256)+((color // 256) % 256)+(color // (256 ** 2)),end=" ")
    if (color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 100:
        click(1020,750)
    color = ctypes.windll.gdi32.GetPixel(hdc, 1140, 750)   
    print((color % 256)+((color // 256) % 256)+(color // (256 ** 2))) 
    if (color % 256)+((color // 256) % 256)+(color // (256 ** 2)) < 100:
        click(1140,750)
    '''   
ctypes.windll.user32.ReleaseDC(0, hdc)
