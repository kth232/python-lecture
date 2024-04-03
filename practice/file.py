"""
infile = open("nowhere.txt", "r")
s = infile.read(10) 
print(s);
infile.close() 
"""
"""
import os.path

outfile = open("phones.txt", "w")

if os.path.isfile("phones.txt"):
	print("동일한 이름의 파일이 이미 존재합니다. ")
else :
	outfile.write("홍길동 010-1234-5678")
	outfile.write("김철수 010-1234-5679")
	outfile.write("김영희 010-1234-5680")

outfile.close()
"""
"""
# 입력 파일 이름과 출력 파일 이름을 받는다. 
infilename = input("입력 파일 이름: ");
outfilename = input("출력 파일 이름: ");

# 입력과 출력을 위한 파일을 연다. 
infile = open(infilename, "r")
outfile = open(outfilename, "w")

# 합계와 횟수를 위한 변수를 정의한다. 
sum = 0
count = 0

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다. 
for line  in infile:
    dailySale = int(line)
    sum = sum + dailySale
    count = count + 1

# 총매출과 일평균 매출을 출력 파일에 기록한다. 
outfile.write("총매출 = "+ str(sum)+"\n")
outfile.write("평균 일매출 = "+ str(sum/count ))

infile.close() 
outfile.close() 
"""
"""
outfile = open("phones.txt", "a")

outfile.write("최무선  010-1111-2222")
outfile.write("정중부  010-2222-3333")

outfile.close()
"""
"""
infile = open("proverbs.txt", "r")
for line  in infile:
	line = line.rstrip()
	print(line);
infile.close() 
"""


