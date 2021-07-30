from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("600x600")
root['background'] = 'black'
passstr = StringVar()
passlen = IntVar()
passlen.set(0)
def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
            '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passstr.set(password)
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
Label(root,bg="red", text="Maari Password Generator", font="Vivaldi 50 italic").pack()
Label(root,bg="blue", text="Enter password length", font="System 25 bold").pack(pady=30)
Entry(root, textvariable=passlen).pack(pady=35)
Button(root,bg="grey", text="Generate Password", font="Fantasy 25 italic", command=generate).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=35)
Button(root,bg="grey", text="Copy to clipboard", font="Retro 25 italic", command=copytoclipboard).pack(pady=7)
root.mainloop()