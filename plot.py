import pylab as plt
plt.figure(1)
plt.subplot()
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
#plt.show()
def f(s):
    if len(s)<=1:
        return s
    return f(f(s[1:]))+s[0]

f("bab")