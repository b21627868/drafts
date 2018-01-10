k = {1,2,3,4,5,12,1,25,2} #kümelerde aynı elemanı girsen bile print ettiğinde yada kullandığında almaz
print(k)
t = (1,2,3,41,2)
print(type(t))
print(type(k))
l =[1,2,34,12,21,1,34,2,4]
k1= {1,24,2,7,8,5,687,56,34,2}
p= set(t)
print(p)
print(type(p))
u=list(k)
print(u)
print(type(u))
k4= set("burak yılmaz")
print(k4)
k5=set("alexdesouza")
print(k5)

print(k-k1)   #fark
print(k|k1)  #union
print(k^k1)  #iki yönlü küme farkı
print(k&k1)  #kesişim kümesi

t ={}
print(type(t))
y= set({})
u = set([])
print(type(y))
print(type(u))