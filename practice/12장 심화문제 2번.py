#12장 심화문제 2번
import pandas as pd

dframe = pd.DataFrame({
   'name' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'horse power' : [130, 250, 190, 300, 210, 220, 170],
    'weight' : [1.9, 2.6, 2.2, 2.9, 2.4, 2.3, 2.2],
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2] })

print("""
12-2-1 name 열 인덱스로 데이터프레임 생성하기""")
dframe = dframe.set_index('name')
print(dframe.head(3)) #A, B, C만 나오게 만들기

print("""
12-2-2 최고 마력을 가진 차종의 행 가져오기""")
print(dframe[dframe['horse power'] == dframe['horse power'].max()])

print("""
12-2-3 마력x연비의 최대값을 가진 차종의 행 가져오기""")
dframe['hp x mile'] = dframe['horse power'] * dframe['efficiency']
print(dframe[dframe['hp x mile'] == dframe['hp x mile'].max()])
