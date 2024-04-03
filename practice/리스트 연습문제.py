"""
# 7장 LAB7-3
population = ["seoul", 9765, "busan", 3441, "incheon", 2954]
print("seoul population: ", population[1])
print("incheon population: ", population[-1])

cities = population[0::2]
print("city list: ", cities)
pops = population[1::2]
print("population sum: ", pops)
"""
"""
# 7장 도전문제 7-3
s = "python is strong"

print(s[0:1])
print(s[-6:])
print(s[:6])
print(s[7:9])
"""
"""
# 7장 리스트 삭제 연습
bts = ["V", "J-Hope", "Suga", "RM", "Jin"]
bts.remove("RM")

if "Suga" in bts:
    bts.remove("Suga")

bts.pop()

del bts[0]
"""
"""
#7장 7-9
alist = ["kim", "park", "lee", "hong"]
blist = list(alist)
blist[0] = "song"
"""
#7장 7-12
numbers = [9, 7, 6, 3, 5, 2, 6, 4, 8]
numbers.sort(reverse=True)
