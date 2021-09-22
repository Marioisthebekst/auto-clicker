import pyautogui, time,keyboard
from tkinter import *

WIN = Tk()
WIN.title("auto clicker ")

def clickedStart():
    time.sleep(5)

    run = True
    intervalInt = None

    try:
        intervalInt = int(text.get())
    except:
        pass

    start = time.time()

    while run:

        if keyboard.is_pressed('d'):
            run = False
            break
        if intervalInt != None:
            if start >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()

label = Label(WIN,text="Click")
label.grid(column= 1,row=0,padx=(120,10))

text = Entry(WIN,width=10)
text.grid(column=1,row=1,padx=(120,10))

button = Button(WIN,text="Start The Bot", command=clickedStart,bg="red",fg="lightskyblue")
button.grid(column=1,row=2,padx=(120,10),pady=(15,10))

WIN.geometry("350x200")
"""
photo = PhotoImage(file= "app.jpg")
WIN.iconphoto(False,photo)
"""


WIN.mainloop()