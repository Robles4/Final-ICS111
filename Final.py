from tkinter import*
import customtkinter 
from PIL import ImageTk, Image
import pygame
import sys

def pygame_start():
    app.destroy()
    print("Paint Rush")


def button_callback():
    print("Button Pressed")

app = customtkinter.CTk()
app.title("paint Rush Main Menu")
app.geometry("400x140")
app.grid_columnconfigure(0, weight=1)

button = customtkinter.CTkButton(app, text="Start Game", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")



app.mainloop()

pygame.init()

wind=pygame.display.set_mode((750,650))
pygame.display.set_caption("Paint Rush")
while True:
         for eve in pygame.event.get():
              if eve.type==pygame.QUIT:
                   pygame.quit()