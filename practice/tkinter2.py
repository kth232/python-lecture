"""
from tkinter import *

window = Tk()
choice = IntVar()

Label(window, 
      text="가장 선호하는 프로그래밍 언어를 선택하시오",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(window, text="Python", padx = 20, variable=choice, value=1).pack(anchor=W)
Radiobutton(window, text="C", padx = 20, variable=choice, value=2).pack(anchor=W)
Radiobutton(window, text="Java", padx = 20, variable=choice, value=3).pack(anchor=W)
Radiobutton(window, text="Swift", padx = 20, variable=choice, value=4).pack(anchor=W)

window.mainloop()
"""
"""
from tkinter import *

window = Tk()
Label(window, text="선호하는 언어를 모두 선택하시오:").grid(row=0, sticky=W)

value1 = IntVar()
Checkbutton(window, text="Python", variable=value1).grid(row=1, sticky=W)
value2 = IntVar()
Checkbutton(window, text="C", variable=value2).grid(row=2, sticky=W)
value3 = IntVar()
Checkbutton(window, text="Java", variable=value3).grid(row=3, sticky=W)
value4 = IntVar()
Checkbutton(window, text="Swift", variable=value4).grid(row=4, sticky=W)

window.mainloop()
"""
"""
from tkinter import *

window = Tk()

lb = Listbox(window, height=8)
lb.pack()
lb.insert(END,"Python")
lb.insert(END,"C")
lb.insert(END,"Java")
lb.insert(END,"Swift")
"""
"""
from tkinter import *
window = Tk()

b1 = Button(window, text="One")
b2 = Button(window, text="Two")
b3 = Button(window, text="Three")
b4 = Button(window, text="Four")

b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=2, column=2)
b4.grid(row=3, column=3)

window.mainloop()
"""
"""
from tkinter import *

window = Tk()

w = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0, y=0)
w = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=20, y=20)
w = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=40, y=40)
w = Label(window, text="박스 #4", bg="yellow", fg="black")
w.place(x=60, y=60)

window.mainloop()
"""
"""
from tkinter import *

# i번째 버튼을 누를 수 있는지 검사한다. 누를 수 있으면 X나 O를 표시한다. 
def checked(i):
    global player
    button = list[i]	# 리스트에서 I번째 버튼 객체를 가져온다. 

	  # 버튼이 초기상태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴한다.
    if button["text"] != "            ":
        return
    button["text"] = "     " + player+"      "
    button["bg"] = "yellow"
    if player=="X":
        player = "O"
        button["bg"] = "yellow"
    else :
        player = "X"
        button["bg"] = "lightgreen"

window = Tk()		# 윈도우를 생성한다.  
player="X"		# 시작은 플레이어 X이다. 
list = []

# 9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다. 
for i in range(9):
    b = Button(window, text="            ", command=lambda k=i: checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)	# 버튼 객체를 리스트에 저장한다. 

window.mainloop()
"""
"""
import tkinter as tk

def startTimer():
    if (running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10, startTimer)

def start():
    global running
    running = True

def stop():
    global running
    running = False

running = False
window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text='시작', bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(window, text='중지', bg="yellow", command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
window.mainloop()
"""



