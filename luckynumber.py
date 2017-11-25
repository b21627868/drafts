import sys
a = (sys.argv[1].split(","))
c = list(a)
liste_uzunluk = len(a)
value = 0
before = 1
i = 0
lucky = 10
start_index=1

def secici():
    global i
    global value
    global start_index
    for i,deger in enumerate(c):
        if int(i) == int(start_index):
            if value == before:
                value = int(c[int(i)+1])
                start_index= int(i)+1
                return value
            else:
                value = int(c[int(i)])
                return value

for j,y in enumerate(c):
    if int(y) < 0:
        del c[int(j)]
secici()

while lucky == 10:
    if value < liste_uzunluk:
        for k in range(1, len(c)+1):
            if int(k) % int(value) != 0:
                continue
            else:
                del c[k-1:len(c)+1:value]
                liste_uzunluk = len(c)
                break
        secici()
        before = int(value)

    else:
        lucky = 9
print("Output :", end=" ")
k = " ".join(c)
print(k)