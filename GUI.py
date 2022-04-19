import tkinter as tk
from encryption import *
from tkinter import filedialog
import os


class GUI:

    def __init__(self):
        self.a = Crypt()
        self.window = tk.Tk()
        self.window.title("Easy Encrypt")
        # self.window.geometry('500x200')
        self.window.iconbitmap("padlock.ico")

        self.make_buttons()

        self.window.mainloop()

    def make_buttons(self):
        """Function to create all button"""
        l1 = tk.Label(self.window, text="Key", font=("Arial", 10), width=20)
        l1.grid(column=0, row=0, pady=10)
        b1 = tk.Button(self.window, text="Generate key", fg="black", command=self.gen_key_button, font=("Arial", 14), width=20)
        b1.grid(column=1, row=0)
        b2 = tk.Button(self.window, text="Load key", fg="black", command=self.load_key_button, font=("Arial", 14), width=20)
        b2.grid(column=2, row=0)

        l2 = tk.Label(self.window, text="Encrypt file", font=("Arial", 10), width=20)
        l2.grid(column=0, row=1, pady=10)
        b3 = tk.Button(self.window, text="Open file", fg="black", command=self.enc_openfile_button, font=("Arial", 14), width=20)
        b3.grid(column=1, row=1)

        l3 = tk.Label(self.window, text="Dencrypt file", font=("Arial", 10), width=20)
        l3.grid(column=0, row=2, pady=10)
        b4 = tk.Button(self.window, text="Open file", fg="black", command=self.dec_openfile_button, font=("Arial", 14), width=20)
        b4.grid(column=1, row=2)

    def openfile(self):
        """Open file popup"""
        currentfile = os.getcwd()
        tk.filedialog.askopenfilenames(initialdir=currentfile)

    def gen_key_button(self):
        """Key generation button"""
        self.a.generate_key()
        tk.messagebox.showinfo('Key', 'Your key as been generated in file key.key')

    def load_key_button(self):
        """Key generation button"""
        currentfile = os.getcwd()
        file = tk.filedialog.askopenfilenames(initialdir=currentfile)
        self.a.read_key(file[0])
        tk.messagebox.showinfo('Key', 'Your key as been loaded')

    def enc_openfile_button(self):
        """pass"""

        if self.a.key == None:
            tk.messagebox.showinfo('Error', 'Generate or load a key first')
            return

        currentfile = os.getcwd()
        file = tk.filedialog.askopenfilenames(initialdir=currentfile)
        self.a.encrypt_file(file[0], "encrypted document.txt")
        tk.messagebox.showinfo('Encryption', 'Your file has been encrypted into "encrypted document.txt"')

    def dec_openfile_button(self):
        """pass"""

        if self.a.key == None:
            tk.messagebox.showinfo('Error', 'Generate or load a key first')
            return

        currentfile = os.getcwd()
        file = tk.filedialog.askopenfilenames(initialdir=currentfile)
        self.a.decrypt_file(file[0], "decrypted document.txt")
        tk.messagebox.showinfo('Decryption', 'Your file has been decrypted into "decrypted document.txt"')


if __name__ == "__main__":
    a = GUI()

