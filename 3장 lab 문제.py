#3장 lab1
import turtle
t=turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리시겠어요?(3-6): "))

for i in range(n):
    t.forward(100)
    t.left(360 // n)

turtle.done()

"""
#3장 lab2
fahrenheit = float(input("화씨온도: "))
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
print("섭씨온도: ", celsius)


#3장 lab3
weight = float(input("몸무게를 Kg단위로 입력하시오: "))
height = float(input("키를 m단위로 입력하시오: "))
bmi = (weight / (height ** 2))
print("당신의 BMI는 ", bmi, "입니다.")

#3장 lab4
money = int(input("투입한 돈: "))
price = int(input("물건값: "))
change = money - price
print("거스름돈: ", change)
coin500s = change // 500
change = change % 500
coin100s = change // 100

print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)
"""
