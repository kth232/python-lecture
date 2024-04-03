x=int(input("첫번째 정수를 입력하시오: "))
y=int(input("두번째 정수를 입력하시오: "))
z=input("연산자를 입력하시오(사칙연산): ")

if z=='+':
    s=x+y
    print("연산결과는", s, "입니다.")

elif z=='-':
    s=x-y
    print("연산결과는", s, "입니다.")

elif z=='*':
    s=x*y
    print("연산결과는", s, "입니다.")

elif z=='/':
    s=x/y
    print("연산결과는", s, "입니다.")

