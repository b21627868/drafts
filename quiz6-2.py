import sys
n = int(sys.argv[1])
copy = n
diamond = [x*"*" for x in range(1, (2*n)+1, 2)] + [x*"*" for x in range((2*n)-3, 0, -2)]
k =2*n
for dia in diamond:
    if len(dia) < k:
        print(((copy - 1) * " ") + dia)
        copy -= 1
        if len(dia)==k-1:
            k = 1
    else:
        copy +=1
        print((copy * " ") + dia)