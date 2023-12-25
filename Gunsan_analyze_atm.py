import pandas as pd                # 데이터를 저장하고 처리하는 패키지
import matplotlib.pyplot as plt    # 그래프를 그리는 패키지
import csv
from matplotlib.dates import DateFormatter, MonthLocator

# csv 파일을 읽어서 DataFrame 객체로 만듦.
f=open('Gunsan_atm.csv',encoding='euc-kr')
data = csv.reader(f)
next(data)
dates = []
pressures = []
for row in data:
    #만약 빈문자('')가 아니라면 리스트에 저장
    if row[-1] != '':
        dates.append(pd.to_datetime(row[2]))
        pressures.append(float(row[-1]))

f.close()

# 그래프를 그리기 위한 준비를 합니다.
fig, ax = plt.subplots(figsize=(10, 5))

# '일시'에 따른 '현지기압' 그래프를 그립니다.
ax.plot(dates, pressures, 'r')

# 그래프의 제목과 x, y축 라벨을 설정합니다.
ax.set_title('Time Series of Atmospheric Pressure in Gunsan', fontsize=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Atmospheric Pressure (hPa)', fontsize=12)

# x축의 날짜 표시 형식을 설정합니다.
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter("%m"))

# 그래프를 보여줍니다.
plt.show()

df = pd.read_csv('Gunsan_atm.csv',encoding='euc-kr')
print(df)

# 기압이 가장 낮은 행을 찾습니다.
min_pressure_row = df[df['현지기압(hPa)'] == df['현지기압(hPa)'].min()]

print("\n\n")

# 기압이 가장 낮은 날의 날짜와 그때의 기압을 출력합니다.
print("최소 기압의 시각: ", min_pressure_row['일시'].values[0])
print("기압: ", min_pressure_row['현지기압(hPa)'].values[0])
