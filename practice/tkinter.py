"""
from tkinter import *

window = Tk()

b1 = Button(window, text="삼육대학교")
b2 = Button(window, text="2018100476")
b3 = Button(window, text="강태현")
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)
b1["text"]="One"
b2["text"]="Two"
b3["text"]="Three"

window.mainloop()
"""
"""
from tkinter import *

def callback():
    button["text"] ="버튼이 클릭되었음!"

window = Tk()
button = Button(window, text="클릭", command=callback)
button.pack(side=LEFT)

window.mainloop()
"""
"""
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root=tk.Tk()

        self.customFont = font.Font(family="Helvetica", size=12)

        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello!", font=self.customFont)
        buttonframe.pack()
        label.pack()

        bigger = tk.Button(root, text="폰트를 크게", command=self.BigFont)
        smaller = tk.Button(root, text="폰트를 작게", command=self.SmallFont)
        bigger.pack()
        smaller.pack()
        root.mainloop()

    def BigFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size+2)

    def SmallFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size-2)

app=App()
"""
"""
from tkinter import *

window = Tk()
photo = PhotoImage(file="해변 배경1.jpeg")
w = Label(window, image=photo).pack(side="right")
message= "바다 가고 싶다."
w2 = Label(window, 
           justify=LEFT,
           padx = 10, 
           text=message).pack(side="left")
window.mainloop()
"""

"""
from tkinter import *

window = Tk()

Label(window, 
		 text="Times Font 폰트와 빨강색을 사용합니다.",
		 fg = "red",
		 font = "Times 32 bold italic").pack()
Label(window, 
		 text="Helvetica 폰트와 녹색을 사용합니다.",
		 fg = "blue",
		 bg = "yellow",
		 font = "Helvetica 32 bold italic").pack()
window.mainloop()
"""

"""
from tkinter import *

window = Tk()
T = Text(window, height=5, width=60)
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의\n텍스트를 표시할 수 있습니다.")
mainloop()
"""
"""
from tkinter import *
window = Tk()
canvas = Canvas(window, width=300, height=200)
canvas.pack()
canvas.create_oval(10, 10, 200, 150)
window.mainloop()
"""
"""
from tkinter import *
window = Tk()

canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas.create_polygon(10, 10, 150, 110, 250, 20, fill="blue")
window.mainloop()
"""
"""
from tkinter import *
window = Tk()

canvas = Canvas(window,  width=300, height=200)
canvas.pack()

img = PhotoImage(file="D:\\starship.png")
canvas.create_image(20, 20, anchor=NW, image=img)

mainloop()
"""
"""
import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id=canvas.create_oval(10, 100, 50, 150, fill="green")

for i in range(100):
   canvas.move(id, 3, 0)
   window.update()
   time.sleep(0.01)
"""
"""
from tkinter import *

w = 500
h = 300

def drawDot( event ):
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   canvas.create_oval( x1, y1, x2, y2, fill = "red" )

window = Tk()
canvas  = Canvas(window, width=w, height=h)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind( "<B1-Motion>", drawDot )

message = Label( window, text = "마우스를 드래그하면 점들이 그려집니다." )
message.pack( side = BOTTOM )
    
window.mainloop()
"""


