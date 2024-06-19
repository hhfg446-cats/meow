import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import pygame

root = tk.Tk()
root.title("Meow")
root.geometry("300x300")

def cat():
    print("meow")

button = tk.Button(root, text="meow", command=cat)
button.pack()

root.mainloop()