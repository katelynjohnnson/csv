import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("death_valley_2018_simple.csv", "r")
open_file1 = open("sitka_weather_2018_simple.csv",'r')

csv_file = csv.reader(open_file,delimiter=',')
csv_file1 = csv.reader(open_file1,delimiter=',')

header_row = next(csv_file)
header_row = next(csv_file1)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


#testing to convert date from string
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(type(mydate))



highs = []
dates = []
lows = []

for rec in csv_file:
    try:
        the_date = datetime.strptime(rec[2],'%Y-%m-%d')
        high = int(rec[4])
        low = int(rec[5])
        
    except ValueError:
        print(f'Missing data for {the_date}')
        #f string = lets you put the variable name in the print statement
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)

#print(highs)
#print(dates)
highs1 = []
lows1 = []
dates1 = []

for rec in csv_file1:
    try:
        the_date = datetime.strptime(rec[2],'%Y-%m-%d')
        high = int(rec[5])
        low = int(rec[6])
        
    except ValueError:
        print(f'Missing data for {the_date}')
        #f string = lets you put the variable name in the print statement
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(the_date)

fig = plt.figure()


plt.subplot(2,1,1)
plt.plot(dates1,highs1,c='red')
plt.plot(dates1,lows1,c='blue')
plt.fill_between(dates1, highs1,lows1,facecolor='blue', alpha=0.1)
plt.title('SITKA AIRPORT, AK US')

plt.subplot(2,1,2)
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates, highs,lows,facecolor='blue', alpha=0.1)
plt.title("DEATH VALLEY, CA US")

plt.suptitle("Temperature comparison between SITKA AIRPORT, US AK and DEATH VALLEY, CA US")

plt.show()
