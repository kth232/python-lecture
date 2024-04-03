infile = open("c:\workplace\student input.txt", "r", encoding='UTF-8')
outfile = open("c:\workplace\student grade.txt", "w") 

lines = infile.readlines()
lines.pop(0) # 첫줄을 지워주기 위한 코드

sum = 0
count = 0

for line in infile:
    process = line.split() # 한 줄에서 공백을 기준으로 분리하여 리스트에 저장
    no = process.pop(0) # 학번 분리하여 저장
    name = process.pop(1) # 이름 분리하여 저장
    stdnscore = int(line)
    sum = sum + stdnscore
    count = count + 1

outfile.write("총점: "+ str(sum)+"\n")
outfile.write("평균: "+ str(sum/count))

infile.close() 
outfile.close()
