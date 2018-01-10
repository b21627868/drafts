found = True
if not found:
    print(21)
else:
    print(12)

def recurMul(a,b):
    if b == 1:
        return a
    else:
        recurMul(a,b-1)
print(recurMul(2,3))
height=72
if height > 100:
    print("space")
elif height > 50:
    print("mesosphere")
elif height > 20:
    print("stratosphere")
else:
    print("troposphere")

print(pow(2,3))
myvar = 1
def outer():
    myvar = 1000
    return inner()
def inner():
    return myvar
print(outer())

a = [1,None,3,{1:12},[],]
print(len(a))
value1=20.5
value2=10
print (value1//value2)

b = [[9,6],[4,5],[7,7]]
x = b[:2]
x[0] = [1,2]
print(b)
print(x)

def f1():
 global x
 x = 1
 print(x)
def f2():
 x = 2
 print(x)
def f3():
 global x
 print(x)
x = 3
f1()
f2()
f3()


def r2d2(a):
 b = True
 for k in range(len(a)):
    b = b and bb8(a,k)
 return b


def bb8(a,k):
 a[k] = a[k]-1
 return a[k] >= 0


a = [1,2,3,4]
print(r2d2(a))
print(a)
print(r2d2(a))
print(a)
def function(value1, value2):
    pass

print(function(1,2))
print(type([1,2]))


def third(x):
 print('S3')
 if x < 0:
    raise IOError()
 elif x > 0:
    raise AssertionError()
 print('E3')

def second(x):
    print('S2')
    try:
        third(x)
    except AssertionError:
        print('C2')
    print('E2')
def first(x):
 print('S1')
 try:
    second(x)
 except IOError:
     print('C1')
 print('E1')

first(-1)
print("++++++++++")
first(1)

k=0
t=0

def female(n):
 # global k
 #k+=1
 if (n == 0):
    return 1
 f = female(n-1)
 return n-male(f)
def male(x):
 #global t
 #t+=1
 if (x == 0):
    return 0
 m = male(x-1)
 return x-female(m)
print(female(3))
print(male(2))
#print(k,t)

def last_name(str):
    return str.split(" ")[1]
print('last_name("Isaac Newton"):',last_name("Isaac Newton"))

a = ["arap","ad","Keops","zemberek","12","11111","ara","we","w","zembe"]
print(sorted(a))
print(a)
a.sort()
print(a)
print(a.sort())

def asd(x):
    return x*x

for i in range(3):
    asd(i)

def split(n):
  return n // 10, n % 10,n*n

print(split(35))



nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
af = [num for num in nums if num % 2 == 0]
print(af)
matrix = [[i+j for j in range(5)] for i in range(5)]
print(matrix)
num_list = [6,4,2,8,9,10,3,2,1,3]
total = float(sum(num_list))

num_list = [i/total for i in num_list]
print(num_list)

alex=[[x,y] for x in range(4) if x > 1 for y in range(5) if y >3 ]
print(alex)
ms = [1,2,3,4,344,34,23,2]
print(ms.pop())
print(ms)

print(["four", "score", "and", "seven", "years"][2])
#print(["four", "score", "and", "seven", "years"][0,2,3])
#print(["four", "score", "and", "seven", "years"][[0,2,3]])
print(["four", "score", "and", "seven", "years"][[0,2,3][1]])

list1 = ["a", "b"]
list2 = list1
list3 = ["a", "b"]
myset =  list1
print(list1)
print(list2)
print(list3)
print(myset)
list2.append("c")
print(list1)
print(list2)
print(list3)
print(myset)
deivid = []
feet = [1,2,3,4,5,6,7,8,9,0]
ronaldo = [x+1 if x >= 4 else x+5 for x in feet if x % 2 == 0]
for x in feet:
    if x % 2 == 0:
        if x >= 4:
            deivid.append(x + 1)
        else:
            deivid.append(x+5)
print(ronaldo)
print(deivid)
beckham = [3,4,5]
drogba = {i:i*i for i in beckham}
print(drogba)
leopold = {v:k for k,v in drogba.items()}
print(leopold)

print(20.5//10)

def getRatios(vect1, vect2):
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError("getRatios called with bad arguments")
    return ratios
try:
    print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0]))
except ValueError as msg:
    print(msg)

b = []
b.append(float("nan"))
print(b)

names = ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Marie Curie", "Charles Darwin", "Louis Pasteur", "Galileo Galilei", "Margaret Mead"]
print("sorted(names):", sorted(names))