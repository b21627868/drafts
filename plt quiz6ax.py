import matplotlib.pyplot as plt
import collections
import sys

occupancy_data = open("occupancy.data", "r")
occupancy = []
not_occupancy = []
date1 = []
date0 = []
dates = []
temp1 = []
temp2 = []
light1 = []
light2 = []
humidity1 = []
humidity2 = []
co2 = []
co22 = []
for data in occupancy_data.read().splitlines():
    if data[-1] == '1':
        occupancy.append(data.split(";"))
    else:
        not_occupancy.append(data.split(";"))

def timer(t):
    global y
    days = t[1].split(" ")
    dayy = days[0].split("-")
    day= dayy[2]
    return day

for i in occupancy:
    date1.append(timer(i))
for i in not_occupancy:
    date0.append(timer(i))
a = collections.OrderedDict(collections.Counter(date1))
b = collections.OrderedDict(collections.Counter(date0))

date = set(date0+date1)
for i in date:
    dates.append(i)
dates.sort()



x = dates
y1 = a.values()
y2 = b.values()
plt.xlabel("Days")
plt.ylabel("# of samples")
plt.plot(x, y1, color="blue", label="Occupied")
plt.plot(x, y2, color="red", label="Not-occupied")
plt.legend(loc='upper left')
plt.savefig("Fig1.pdf")

def choose(value):
        temp1.append(float(value[2]))
        humidity1.append(float(value[3]))
        light1.append(float(value[4]))
        co2.append(float(value[5]))


def choose1(value):
        temp2.append(float(value[2]))
        humidity2.append(float(value[3]))
        light2.append(float(value[4]))
        co22.append(float(value[5]))


for b in occupancy:
    choose(b)
for bb in not_occupancy:
    choose1(bb)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

ax0.set_title('Temperature\n')
ax0.hist(temp1, bins=len(temp1)//100, color="blue",stacked=True)

ax1.set_title("Humidity (%)\n")
ax1.hist(humidity1, bins=len(humidity1)//100, color="red")

ax2.set_title('Light\n')
ax2.hist(light1, bins=len(light1)//100, color="green")

ax3.hist(co2, bins=len(co2)//100, color="purple")
ax3.set_title('Co2\n')
fig.tight_layout()
plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

ax0.set_title('Temperature\n')
ax0.hist(temp2,  histtype='bar', color="blue", bins=len(temp2)//1000)

ax1.set_title("Humidity (%)\n")
ax1.hist(humidity2, bins=len(humidity2)//1000,  histtype='bar', color="red")

ax2.set_title('Light\n')
ax2.hist(light2, bins=len(light2)//1000, histtype='bar', color="green")

ax3.hist(co22, bins=len(co22)//1000, histtype='bar', color="purple")
ax3.set_title('Co2\n')
fig.tight_layout()
#plt.figure(figsize=(6,7))
#plt.show()
