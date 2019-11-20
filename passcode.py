# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:29:13 2019

@author: Deepak
"""

import random as r
import string as s
import tkinter as tk
from tkinter import messagebox

def generate_passcode(size):
    passCode = '' . join(r.choice(s.ascii_uppercase + s.ascii_lowercase + s.digits) for n in range(size))
    return passCode

def get_passcode():
    pwd = generate_passcode(10)
    messagebox.showinfo( "Passcode", pwd )

def close_window (): 
    top.destroy()


top = tk.Tk()
top.geometry("200x300")

frame = tk.Frame(top)
frame.pack()

button = tk.Button(frame, 
                   text="Quit", 
                   fg="red",
                   command=close_window)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Generate Passcode",
                   fg="black",
                   command=get_passcode)
slogan.pack(side=tk.LEFT)

top.mainloop()