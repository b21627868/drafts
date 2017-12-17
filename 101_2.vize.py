for i in range(1,10,2):
    print(i)

def ping(n):
    if n <0:
        return "pinged"
    else:
        return "1" + pong(n-2)

def pong(m):
    if m<0:
        return "Ponged"
    else:
        return "0"+ ping(m-1)

print(pong(4))
print(ping(6))

def bizarre(a):
    a[1]= "and"
    (a[0],a[2])=(a[2],a[0])
    print(a)
    b =a
    b.extend([42,"summer","morty",2017])
    b.pop()
    print(b)
    c = []+b
    print(c)
    c[1:-1]=["hello","world"]
    return c

a = [25,'10',"rick"]
print(bizarre(a))
print(a)

lst=["i"+" "+2*"*" if i %2 == 0 else "i"+""+"*" for i in range(10,0,-1)]
for e in lst:
    print(e)


def read(x):
    a =0
    b =9
    while x>b:
        c= x%10
        if c**2<=b:
            a+=1
        x=x//10
    return a==x and x>0
print(read(11))

def mystery_print(filename):
    file = open(filename,"r")
    lst=[]
    for line in file:
        for word in line.split("A"):
            if len(word)>1:
                lst.append(word)
    file.close()
    lst2=sorted(lst,reverse=True)
    for word in lst2:
        print(word)

print(mystery_print("calis"))

def al(a,b):
    while a>b:
        for c in range(1,8,b):
            print(a,b,c)
            a = a-3
        b +=2
print(al(12,4))