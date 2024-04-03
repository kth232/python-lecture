"""
def print_company_address():
    print("삼육대학교")
    print("노원구")
    print("010 8704 9085")

def print_star():
    print('****************')

def print_address2(name, address):
    print("이름: ", name)
    print("주소: ", address)

print_star()
print_address2("홍길순", "부산광역시 남구")
print_star()
"""

def calculate_area(radius):
    area = 3.14*radius**2
    return area

c_area = calculate_area(5.0)
print(c_area)

area_sum = calculate_area(5.0) + calculate_area(10.0)
print(area_sum)
