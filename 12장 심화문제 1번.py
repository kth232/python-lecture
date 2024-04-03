#12장 심화문제 1번
import pandas as pd

weather = pd.read_csv('c:/workplace/weather.csv', index_col = 0, encoding='CP949')
print("""
12-1-1 앞 행 3개 가져오기""")
print(weather.head(3))
print("""
12-1-1 뒤 행 3개 가져오기""")
print(weather.tail(3))

print("""
12-1-2 하나의 행 가져오기(2015년 6월 6일)""")
print(weather.loc['2015-06-06'])

print("""
12-1-3 최고 평균기온 가져오기""")
print(weather['평균기온'].max())

print("""
12-1-4 최고 평균기온인 날짜의 행 가져오기""")
print(weather[weather['평균기온'] == weather['평균기온'].max()])

print("""
12-1-5 평균기온이 30도 이상인 행 가져오기""")
print(weather[weather['평균기온'] >= 30.0 ])



