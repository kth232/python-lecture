import pandas as pd
import matplotlib.pyplot as plt

gcrime_o = pd.read_csv('c:/workplace/cyber gambling crime_occurrence.csv', index_col = 0) # 도박범죄_발생 파일 열기

"""
fcrime_o = pd.read_csv('c:/workplace/cyber fraud crime_occurrence.csv', index_col = 0) # 사기범죄_발생 파일 열기
fcrime_a = pd.read_csv('c:/workplace/cyber fraud crime_arrest.csv', index_col = 0) # 사기범죄_검거 파일 열기

gcrime_a = pd.read_csv('c:/workplace/cyber gambling crime_arrest.csv', index_col = 0) # 도박범죄_검거 파일 열기
"""

gcrime_o.plot(kind='bar', color = ('m', 'orange', 'r'), width = 0.4, figsize = (7, 4), alpha = 0.4) #막대 그래프, 변수 이름 주의

"""
fcrime_a.plot(kind='bar', color = ('#CADA72', '#ABD9C5', '#F4D451'), width = 0.4, figsize = (7, 4), alpha = 0.8) #막대 그래프, 변수 이름 주의
gcrime_a.plot(kind='bar', color = ('#EC8260', '#FFFF66', '#F0CB85'), width = 0.4, figsize = (7, 4), alpha = 0.8) #막대 그래프, 변수 이름 주의
fcrime_o.plot(kind='bar', color = ('#00ACEE', 'purple', 'blue'), width = 0.4, figsize = (7, 4), alpha = 0.4) #막대 그래프, 변수 이름 주의

"""

plt.title("cyber gambling crime occurrence by year", fontsize = 20) # 제목 설정 fraud/gambling, arrest/occurrence
plt.xlabel("type",fontsize = 16) # x축 이름 만들기
plt.xticks(rotation =0)
plt.ylabel("number of occurrence", fontsize = 16) # arrest/occurrence y축 이름 만들기

plt.legend() # 범례
plt.show()

