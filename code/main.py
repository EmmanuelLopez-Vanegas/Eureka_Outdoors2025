#Modules
import random
import tkinter
import datetime 
from tkinter import filedialog

#List of outdoor items
items = ["stop sign", "flower", "clouds"]

#drawing window with tkinter, some basic setup
root = tkinter.Tk()
root.title("testing testing one two three *taps mic* is this thing on")

#UI design
file_upload_button = tkinter.Button(root, text="+", padx=5, pady=5)
file_upload_button.grid(row=1, column=1, padx=18)
#looping window to allow for user interaction
root.mainloop()
