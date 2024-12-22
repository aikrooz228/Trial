import tkinter
from tkinter import *

window = Tk()

choose_language=tkinter.Label(window,text="Enter a language ")

choose_language.pack()

name_text_box=tkinter.Entry(window)
name_text_box.pack()

window.geometry("700x600")

window.title("Welcome to Hausa World")

window.mainloop()