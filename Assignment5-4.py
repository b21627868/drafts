import matplotlib
matplotlib.use('Agg')
import pylab as plt
import collections
import numpy as np
diabetes = open("diabetes.data", "r")
dia = []
max_preg = []
min_preg = []
max_body = []
min_body = []
for line in diabetes.readlines():
    line = line.strip("\n").split(";")
    dia.append(line)

ages = [int(age[7]) for age in dia if int(age[2]) >= 90]
blood = [real for real in dia if int(real[2]) >= 90]
for List in blood:
    ratio = float(List[0])/float(List[7])
    ratio1 = float(List[5])/float(List[7])
    max_preg.append(ratio)
    max_body.append(ratio1)
    if float(List[0]) > 0:
        min_preg.append(ratio)
    if float(List[5]) > 0:
        min_body.append(ratio1)

pregnancy = (max_preg.index(max(max_preg)))
not_pregnancy = (max_preg.index(min(min_preg)))
body_max = (max_body.index(max(max_body)))
body_min = (max_body.index(min(min_body)))

value1 = (max_preg.index(max(max_preg)))
value2 = float(blood[pregnancy][7])
value3 = (max_preg.index(min(min_preg)))
value4 = float(blood[not_pregnancy][7])
value5 = (max_body.index(max(max_body)))
value6 = float(blood[body_max][7])
value7 = (max_body.index(min(min_body)))
value8 = float(blood[body_min][7])

plt.xlabel("Instances")
plt.ylabel("Ages")

t = np.arange(1, len(ages), 5)
plt.xticks(t)
#plt.annotate("max(#pregnancy/age)", xy=(10.5, 42), xytext=(20, 43), arrowprops=dict(facecolor='red', width=4))
#plt.annotate("min(#pregnancy/age)", xy=(28, 45), xytext=(30, 50), arrowprops=dict(facecolor='red', width=4))
#plt.annotate("min(#Body mass index /age)", xy=(39, 60), xytext=(34, 62), arrowprops=dict(facecolor='green', width=4))
#plt.annotate("max(#Body mass index /age)", xy=(52, 22), xytext=(42, 25), arrowprops=dict(facecolor='green', width=4))
plt.annotate("max(#pregnancy/age)", xy=(value1, value2), xytext=(value1+4, value2+4), arrowprops=dict(facecolor='red', width=4))
plt.annotate("min(#pregnancy/age)", xy=(value3, value4), xytext=(value3+4, value4+4), arrowprops=dict(facecolor='red', width=4))
plt.annotate("min(#Body mass index /age)", xy=(value7, value8), xytext=(value7-4, value8+2), arrowprops=dict(facecolor='green',width=4))
plt.annotate("max(#Body mass index /age)", xy=(value5, value6), xytext=(value5-5, value6+4), arrowprops=dict(facecolor='green',width=4))

plt.plot(range(len(ages)), ages, color="Blue")
plt.savefig("Fig1.pdf")
plt.show()
real_dia = []
no_dia = []
for l in dia:
    if l[-1] == "1":
        real_dia.append(l[7])
    else:
        no_dia.append(l[7])
real_dia = collections.Counter(real_dia)
no_dia = collections.Counter(no_dia)

for k in sorted(real_dia.keys()):
    if k in no_dia.keys():
        pass
    else:
        no_dia[k] = 0
for key,value10 in no_dia.items():
    if key in real_dia.keys():
        pass
    else:
        real_dia[key] = 0
reall_dia = sorted(real_dia.items())
noo_dia = sorted(no_dia.items())


year_list = []
x_axis_diabet = []
x_axis_diabet_not = []
for tupple in reall_dia:
    year_list.append(2017-int(tupple[0]))
    x_axis_diabet.append(tupple[1])

for n in noo_dia:
    x_axis_diabet_not.append(n[1])

year_list = list(reversed(year_list))

year_range = [i for i in range(len(year_list))]

x_axis_diabet = list(reversed(x_axis_diabet))
x_axis_diabet_not = list(reversed(x_axis_diabet_not))

bar_width = 0.2
b= []
a = year_range.copy()
for ns in a:
    b.append(ns+bar_width)


fig, ax = plt.subplots()
plt.bar(year_range, x_axis_diabet, bar_width, label="Diabete", color="Blue",align="center")
plt.bar(b, x_axis_diabet_not, bar_width, label="Not-Diabete", color="red",align="edge")
plt.xticks(year_range, year_list)
plt.xticks(rotation=65, fontsize=7,)
plt.legend(loc='upper left')
plt.xlabel('Years')
plt.ylabel('# of patients')
plt.tight_layout()
plt.savefig("Fig2.pdf")

plt.show()

diabetes.close()