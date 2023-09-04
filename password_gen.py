import string
import tkinter
from tkinter import *
import tkinter.messagebox
import pyperclip, random

root = tkinter.Tk()
root.title("Password Generator")
root.geometry("650x650+400+100")
root.resizable(False, False)

passstr = StringVar()
passlen = IntVar()
passlen.set(0) # This is initially set to zero.

def generate():
      pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', ',']
      password = ""

      for x in range (passlen.get()):
            password = password + random.choice(pass1)
      passstr.set(password)

def copytoclipboard():
      random_password = passstr.get()
      pyperclip.copy(random_password)

Label(root).pack()
Label(root, text="Enter Password Length").pack(pady=4)
Entry(root, textvariable=passlen).pack(pady=4)

Button(root, text="Generate Password", command=generate).pack()
Entry(root, textvariable=passstr).pack(pady=4)
Button(root, text="Copy to Clipboard", command=copytoclipboard).pack()
root.mainloop()