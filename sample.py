import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.dates import DateFormatter, MonthLocator

# 원하는 파일 선택
f=open('Gunsan_atm.csv',encoding='euc-kr')
data = csv.reader(f)
next(data)

#날짜와 기압 데이터 저장
dates = []
pressures = []

for row in data:
    if row[-1] != '':
        dates.append(pd.to_datetime(row[2]))
        pressures.append(float(row[-1]))

f.close()

# 그래프 그리기 위한 준비
fig, ax = plt.subplots(figsize=(10, 5))

# '일시'에 따른 '현지기압' 그래프
ax.plot(dates, pressures, 'r')

# 그래프의 제목, x, y축 라벨 설정
ax.set_title('Time Series of Atmospheric Pressure in Gunsan', fontsize=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Atmospheric Pressure (hPa)', fontsize=12)

# x축의 날짜 표시 설정
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter("%m"))

plt.show()

df = pd.read_csv('Gunsan_atm.csv',encoding='euc-kr')
print(df)
print("\n\n")

# 기압이 가장 낮은 행을 탐색
min_pressure_row = df[df['현지기압(hPa)'] == df['현지기압(hPa)'].min()]

# 기압이 가장 낮은 날의 날짜,그때의 기압 출력
print("최소 기압의 시각: ", min_pressure_row['일시'].values[0])
print("기압: ", min_pressure_row['현지기압(hPa)'].values[0])


