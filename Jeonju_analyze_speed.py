import pandas as pd                # 데이터를 저장하고 처리하는 패키지
import matplotlib.pyplot as plt    # 그래프를 그리는 패키지
import csv
from matplotlib.dates import DateFormatter, MonthLocator

# csv 파일을 읽어서 DataFrame 객체로 만듦.
f=open('Jeonju_windspeed.csv',encoding='euc-kr')
data = csv.reader(f)
next(data)
dates = []
speed = []
for row in data:
    #만약 빈문자('')가 아니라면 리스트에 저장
    if row[-1] != '':
        if row[-1][0] == '.':
            dates.append(pd.to_datetime(row[2]))
            speed.append(float(row[-1]))
        else:
            dates.append(pd.to_datetime(row[2]))
            speed.append(float(row[-1]))

f.close()

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(dates, speed, 'r')

# 그래프의 제목과 x, y축 라벨을 설정합니다.
ax.set_title('Time Series of wind speed in Jeonju', fontsize=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Wind speed (m/s)', fontsize=12)

# x축의 날짜 표시 형식을 설정합니다.
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter("%m"))

# 그래프를 보여줍니다.
plt.show()

df = pd.read_csv('Jeonju_windspeed.csv',encoding='euc-kr')
print(df)