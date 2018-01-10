L= [1,3,5,8,12,4634,213,85,23,3]
Y= ["12",124,"122",5,"dss","asdas","h",1]
c= ["asd","gddsv","sdgbsd","fgmnf","21","45","1","1241","qzs","w","asdf"]

k=L.sort()
#Y.sort()
c.sort()
print(L)
print(Y)
print(c)
print(k)

a= [1,3,5,8,12,4634,213,85,23,3]
b= ["12",124,"122",5,"dss","asdas","h",1]
t= ["asd","gddsv","sdgbsd","fgmnf","21","45","1","1241","qzs","w","asdf"]

u =sorted(a,reverse=True)
f=sorted(a,reverse=False)
print(a)
print(u)
print(f)

print(t)
x = sorted(t,reverse=True)
print(x)
from operator import itemgetter
student_score = ('Robert', 8)

print(itemgetter(0)(student_score))
print(itemgetter(1)(student_score))

student_scores = [('Robert', 8), ('Alice', 9),
('Tina', 7)]
print(itemgetter(0)(student_scores))
k1=sorted(student_scores, key=itemgetter(0) )
k2=sorted(student_scores, key=itemgetter(1) )
print(k1)
print(k2)


def bubbleSort(alist):
        for passnum in range(len(alist)-1,0,-1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            alist[position]=currentvalue
blist = [54,26,93,17,77,31,44,55,20]
insertionSort(blist)
print(blist)

def merge(left, right):
    result = []
    (i,j) = (0, 0)
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i<len(left):
        result.append(left[i])
        i = i + 1
    while j<len(right):
        result.append(right[j])
        j = j + 1
    return result

print(15/2)
print(15//2)