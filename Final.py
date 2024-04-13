from tkinter import*
from PIL import ImageTk, Image
import pygame
import sys

def pygame_start():
    root.destroy()
    print("Test")


root=Tk()
#photo = Image.open("Final-Project/Assets/BackgroundImage.png")
photo = ImageTk.PhotoImage(Image.open("Final-ICS111/Assets/Canvas.png").resize((1750, 1750)))

w = Label(root, image=photo)
w.pack()
root.title('Paint Rush')
root['bg']='black'
def tab():
    def tab1():
        ct1 = Canvas(root, bg='orange', width=2000, height=1000)
        ct1.place(x=1, y=1)
        q = Label(ct1, image=photo)
        q.pack()
        label1 = Label(root, text='How to Play', bg='orange' ,font=('Arial', 30))
        label1.place(x=450, y=100)
        tab()
    def tab2():
        ct2 = Canvas(root, bg='pink', width=2000, height=1000)
        ct2.place(x=1, y=1)
        e = Label(ct2, image=photo)
        e.pack()
        label2 = Label(root, text='Settings', bg='pink' ,font=('Arial', 30))
        label2.place(x=450, y=100)
        tab()
    c1 = Canvas(root, bg='tan', width=2000, height=100)
    c1.place(x=1, y=550)
    tab1_b = Button(root, text='How to Play', font=('Arial', 20), command=tab1)
    tab1_b.place(x=400, y=567)
    tab2_b = Button(root, text='Settings', font=('Arial', 20), command=tab2)
    tab2_b.place(x=800, y=567)
    tab3_b = Button(root, text='Start Button', font=('Arial', 20), command=pygame_start)
    tab3_b.place(x=1120, y=567)
tab()
root.mainloop()

pygame.init()

wind=pygame.display.set_mode((750,650))
pygame.display.set_caption("Paint Rush")
while True:
         for eve in pygame.event.get():
              if eve.type==pygame.QUIT:
                   pygame.quit()
                   sys.exit() 