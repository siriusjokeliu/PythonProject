import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = '../data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    """获取数据"""
    dates, highs,lows =[],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'Missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    """绘制图形"""
    fig = plt.figure(dpi=128,figsize=(9,6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates,lows,c='blue')
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    """设置图形注释"""
    plt.title("Daily high and low temperature, 2014 CA",fontsize = 24)
    plt.xlabel('',fontsize=20)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis='both', which='major',labelsize=16)
    plt.show()
