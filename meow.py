import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

sound_file = 'meow.wav'

def cat():
    print("meow")
    pygame.mixer.Sound(sound_file).play()

root = tk.Tk()
root.title("Meow")
root.geometry("300x300")

button = tk.Button(root, text="click to meow", command=cat)
button.pack()

root.mainloop()
