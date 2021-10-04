import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=',')

header_row = next(csv_file)

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


fig = plt.figure()
plt.title("Daily highand low temperature - 2018\nDeath Valley", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis="both",which = "major", labelsize = 12)
fig.autofmt_xdate()

plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows, c="blue", alpha=0.5)

plt.fill_between(dates,highs,lows, facecolor="blue", alpha = 0.1)

plt.show()

plt.subplot(2,1,1)
plt.plot(dates,highs,c='red')
plt.title('Highs')

plt.subplot(2,1,2)
plt.plot(dates,lows,c='blue')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
