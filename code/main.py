#Modules
import random
import tkinter
import datetime 
from tkinter import filedialog

#List of outdoor items
items = ["stop sign", "flower", "clouds"]

#drawing window with tkinter, some basic setup
root = tkinter.Tk()
root.title("Real life scavenger hunt")

def upload_image():
    pass

#UI design
file_upload_button = tkinter.Button(root, text="+", padx=5, pady=5, command=upload_image())
file_upload_button.grid(row=1, column=1, padx=18)

Label_one = tkinter.Label()
#looping window to allow for user interaction
root.mainloop()
