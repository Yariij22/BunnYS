import keyboard
import time
from tkinter import *

from threading import Thread

# Создаем графический интерфейс

gui = Tk(className='Python Examples - Window Color')
# set window size
gui.geometry("500x100")
gui.configure(bg='black')
gui.title("BunnyUp")

# Создаем функции для кнопок



def start_bunnyhop ():#line:160
    def OOOOO00OO00000O00 ():#line:161
        pass #line:165
    Thread (target =OOOOO00OO00000O00 ).start ()#line:167
    print ("BunnyHop запущен.")#line:168
def stop_bunnyhop ():#line:170
    pass #line:174
    gui .quit ()#line:175
start_button =Button (gui ,text ="Start bunnyhop",command =start_bunnyhop ,bg ='orange')#line:182
start_button .pack (pady =10 )#line:183
stop_button =Button (gui ,text ="Stop bunnyhop",command =stop_bunnyhop ,bg ='red')#line:185
stop_button .pack (pady =10 )#line:186
gui .mainloop ()