import os
import time
from tkinter import *  # for ui
# from voice import take_command,talk
from PIL import ImageTk, Image
from tkinter import messagebox

from codeenvsetup import codenv

# creating the application main window.   { open so many windows simultaneusly }
top = Tk()
top.geometry("800x450")

# Adding Text
Label(
    height=15,
    text="Welcome to Dasamoolam's world ",
    foreground="red",  # Set the text color to red
    background="black"  # Set the background color to black
).place(x=50, y=80)

def manager(cmd):
    print(cmd)  
    if 'play' in cmd:
        if 'love' in cmd:
            os.system("video.mp4")
        if 'sad' in cmd:
            playsad()

    elif 'find' in cmd:
        if 'bug' in cmd:
            findbug()
            playsad()
    

def playsad():
    os.system("sad.mp4")


def findbug():
    import pywhatkit as pkt
    copy = Tk()
    copy.withdraw()
    number = copy.clipboard_get()
    query = 'https://stackoverflow.com/search?q=' + number
    print(query)
    pkt.search(query)        

def start():  

    root = Tk()
    root.attributes('-topmost',True)
    e = Entry(root)
    e.pack()

    def printtext():
        string = e.get() 
        manager(string)

    b = Button(root,text='okay',command=printtext)

    b.pack(side='bottom')
    e.focus_set()


Button(
    text="START DAMU AI ASSISTANT",
    command = start,
    height=1,
    bg="blue",
    fg="yellow",
).place(x = 0,y = 0) 




# Create a photoimage object of the image in the path
image1 = Image.open("index.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=360, y=80)

time.sleep(3)
start()
time.sleep(6)
# codenv()
time.sleep(6)
# Entering the event main loop   { under every ui code }
top.mainloop()  

