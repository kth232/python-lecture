import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=800, height=500)
canvas.pack()

img = PhotoImage(file = 'c:\workplace\sw car.png')
id=canvas.create_image(20, 20, anchor=NW, image=img)
canvas.create_text(400, 350, text='3초 후 자동차가 출발합니다.', font=(20))

time.sleep(3) #3초 정지 후 출발
for i in range(100): # 원을 움직이고 윈도우를 다시 그림
    canvas.move(id, 3, 0) #move(움직이고자 하는 객체, x방향, y방향)
    window.update() # 화면 다시 그림
    time.sleep(0.05) # 일시정지
