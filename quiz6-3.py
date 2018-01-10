import matplotlib.pyplot as plt
import collections

occupancy_data = open('occupancy.data', "r")
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
    day = dayy[2]
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
#plt.savefig("Fig1.pdf")
plt.show()

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
#locs, labs = plt.xticks()
plt.subplot(221)
plt.title('Temperature\n')
plt.hist(temp1, bins=len(temp1)//100, color='blue', )

plt.subplot(222)
plt.title("Humidity (%)\n")
plt.hist(humidity1, bins=len(humidity1)//100, color='red')

plt.subplot(223)
plt.title('Light\n')
plt.hist(light1, bins=len(light1)//100, color='green')
#plt.xticks(np.arange(0,500,100)) mesela plt.xticks(a,b,rotation=vertical) yazarsak a daki değerleri b dekilerle değiştirip dikey yazar
plt.subplot(224)
plt.title('Co2\n')
plt.hist(co2, bins=len(co2)//100, color='purple')

#Bins are the number of intervals you want to divide all of your data into,
# such that it can be displayed as bars on a histogram.
# A simple method to work our how many bins are suitable is to take the square root of the total number of values in your distribution.
#The bins parameter tells you the number of bins that your data will be divided into. You can specify it as an integer or as a list of bin edges.
plt.suptitle("Occupied")
plt.tight_layout()
#plt.savefig("Fig2.pdf")
plt.show()

plt.subplot(221)
plt.title('Temperature\n')
plt.hist(temp2, bins=len(temp2)//1000, color='blue')

plt.subplot(222)
plt.title("Humidity (%)\n")
plt.hist(humidity2, bins=len(humidity2)//1000,  color='red')

plt.subplot(223)
plt.title('Light\n')
plt.hist(light2, bins=len(light2)//1000,  color='green')

plt.subplot(224)
plt.title('Co2\n')
plt.hist(co22, bins=len(co22)//1000,  color='purple')
plt.suptitle("Not-occupied")
plt.tight_layout()
#plt.savefig("Fig3.pdf")
plt.show()