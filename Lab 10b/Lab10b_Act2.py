# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         JP Moore
# Section:      519
# Assignment:   Lab 10b-Act2
# Date:         17 November 2021
#

import matplotlib.pyplot as plt
import numpy as np

temps = []
winds = []
rains = []
mins = []
maxes = []
monthTemps = [[],[],[],[],[],[],[],[],[],[],[],[]] #12 lists. If you try to multiply an empty list by 12 it doesn't work
monthMins = [[],[],[],[],[],[],[],[],[],[],[],[]]
monthMaxes = [[],[],[],[],[],[],[],[],[],[],[],[]]
#getting data
with open("CllWeatherData.csv") as data:
    first = True
    for line in data:
        if not first:
            elements = line.split(",")
            temps.append(float(elements[3]))
            winds.append(float(elements[1]))
            if elements[2] != "0":
                rains.append(float(elements[2]))
            mins.append(elements[5])
            maxes.append(elements[4])
            #put temperatures into "months"
            month = int(elements[0].split("/")[0]) - 1
            monthTemps[month].append(int(elements[3]))
            monthMins[month].append(int(elements[5]))
            monthMaxes[month].append(int(elements[4]))
        else:
            first = False
            # print(line.split(",")[5])
            
        
fig, ax1 = plt.subplots()
plt.xlabel("date")
plt.title("Average Temperature and Wind Speed")
ax1.plot(temps, color="red")
plt.ylabel("Average Temperature, F")
plt.legend(["Temp avg"])
ax2 = ax1.twinx()
ax2.plot(winds, color="blue")
plt.ylabel("Average Wind Speed, mph")
plt.legend(["Wind avg"])
plt.show()

#Histogram of precipitation
plt.hist(rains, 50)
plt.title("Histogram of precipitation")
plt.xlabel("Precipitation, in")
plt.ylabel("Number of days")
plt.show()

#scatter plot of wind speed vs min temp
plt.scatter(mins, winds, s=5, color="black")
plt.xticks(np.arange(0, 70, 10))
plt.title("Average Wind Speed vs Minimum Temperature")
plt.xlabel("Minimum Temperature, F")
plt.ylabel("Average Wind Speed, mph")
plt.show()

#Average Temperature by Month
mMeans = []
mMaxes = []
mMins = []
for l in monthTemps: # find the average temperature of each month
    s = 0
    count = 0
    for t in l:
        s += t
        count += 1
    mMeans.append(s / count)
for l in monthMaxes:
    mx = -200 #if the temperature is ever below -200 degrees for every day of a month, this code will break.
    for t in l:
        if t > mx:
            mx = t
    mMaxes.append(mx)
for l in monthMins:
    mn = 200
    for t in l:
        if t < mn:
            mn = t
    mMins.append(mn)
plt.bar(range(1, 13) , mMeans, color="orange", alpha=0.6)
plt.plot(range(1, 13), mMaxes, color="red")
plt.plot(range(1, 13), mMins, color="blue")
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.title("Average Temperature by Month")
plt.legend(["High T", "Low T"])
plt.show()