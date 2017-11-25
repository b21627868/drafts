def dict_roll(dct):
    sums = []
    schucki1 = collections.OrderedDict()            # değişmeyen dictionary kullanmak isteyip değerleri yada keyleri belirli sayıda shift yapmak istiyosan
    shift_values = collections.deque(dct.keys())
    shift_values.rotate(n)
    for deger in shift_values:
        for value in dct.values():
            if value in sums:
                continue
            schucki1[deger]=value
            sums.append(value)
            break
    return schucki1

def dict_roll(dct):
    before = []
    values = []
    dct1 = {}                                      #dictionarynin sırası önemli değilse ve belirli sayıda shiftihng yapmak istiyosan
    print(dct)
    for key,value in dct.items():
        values.append(value)
    shift_values = rotate(values,n)
    print(shift_values)
    for deger in shift_values:
        for key in dct.keys():
            if key in before:
                continue
            dct1.update(dict({key: deger}))
            before.append(key)
            print(dct1)
            break
    return dct1

schucki1 = collections.OrderedDict()    #boş bir ordereddict yapma yolu

def rotate(l, n):
    return l[-n:] + l[:-n]  #listeyi belirli sayıda kaydırmak

def hex2bin(str):
   bin =
   aa = ''                                      #hexadecimalden binarye çevirme
   for i in range(len(str)):
      aa += bin[atoi(str[i],base=16)]
   return aa

  def dict_roll(dct, deger):
        shift_values = collections.deque(dct.values())      #dictrollun başka hali
        shift_values.rotate(n)
        dct = dict(zip(dct.keys(), shift_values))
        return dct

Palindrome = input("Bir kelime giriniz:")
def palindrome():
    for i in range(len(Palindrome)//2):
        if Palindrome[i] == Palindrome[-i-1]:   #palindrome mu değil mi anlama fonksiyonu
            continue
        else:
            y = "Palindrom degil",
            return y
    dogru="Palindromdur"
    return dogru
print(palindrome())

L = list(input("sayılar giriniz:").split(","))
L.sort()
def bulucu():
    n = int(input("bir sayı giriniz"))
    if n <= len(L):
        return int(L[n-1])
    else:
        while n >= len(L):
            return bulucu()

def hex2binanother(num):
    bit = []
    if num == 0:
        return '0000'               #hexden binary e çevirme başka yolu
    while num > 0:
        bin_str = str(num % 2)
        bit.append(bin_str)
        num = num // 2
    bin_str = bit[::-1]
    if len(bin_str) != 4:
        if len(bin_str) == 3:
            bin_str = "0" + "".join(bin_str)
        if len(bin_str) == 2:
            bin_str = "00" + "".join(bin_str)
        if len(bin_str) == 1:
            bin_str = "000" + "".join(bin_str)
        return bin_str
    else:
        return "".join(bin_str)


def to_int(bin):
    global n
    for y, b in enumerate(reversed(bin)):            #2 complements olarak çevirmenin yolu
        if b == '1':
            if y != (len(bin)-1):
                n += 2**y
            else:
                n -= 2**y
    return n

def transformer(a):
    global Union
    temp = a                                             # binaryden hexa ya çevirme
    new_int, power = 0, 0
    if temp == "":
        return
    else:
        while len(temp) > 0:
            bit = int(temp[-1])
            new_int = new_int + bit * 2 ** power
            temp = temp[:-1]
            power += 1
        Union.append(str(new_int))

def split(n):
  return n // 10, n % 10  #verilen sayıyı parçalamak tuple yapar son basamağını alır geri kalanını bir bütün olarak tutar

def fact(n):
    if n == 0:
        return n                        #recursive faktöriyel
    else:
        return n*fact(n-1)

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return  s[0] == s[-1] and isPal(s[1:-1])    #return şeklini gör diye koydum bunu

def fib(n):
    if n == 0:
        return 1
    elif n == 1:                     #fibonacci dizisi
        return 1
    else:
        return fib(n-2) + fib(n-1)

def even(n):
    if n == 0:
        return True
    else:
        return odd(n - 1)           #arka arkaya mutual recursion örneği

def odd(n):
    if n == 0:
        return False
    else:
        return even(n - 1)

import sys

numberList = [int(i) for i in str(sys.argv[1]).split(',')]


def findGreatestElement(greatestVal, numberList):       								# recursion that divides problem until last element is reached
    if len(numberList) == 1:
        return numberList[0]                            								# returns the last element of the list -numberList
    else:
        return max(numberList[0], findGreatestElement(greatestVal, numberList[1:])) 	# compares then returns maximum element. see example below
