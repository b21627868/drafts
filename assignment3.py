import sys
import collections
hurap_file = open(sys.argv[1], "r")

schuckscii_file = open(sys.argv[2], "r")

virus_codes_file = open(sys.argv[3], "r")

representations = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                   '7': '7', '8': '8', '9': '9', '10': "A", '11': "B", '12': "C",
                   '13': "D", '14': "E", '15': "F"}
alex = []
substituted = {}
w = 0
for i in schuckscii_file.readlines():
    i = i.strip("\n").split("\t")
    alex.append(i)
    del alex[w][2]
    w +=1
schucki = collections.OrderedDict(alex)
print(alex)
print(schucki)
Union = []
Alien = []
Encrypted = []
Encrypted_2 = []
Dencrytpted = []
Dencrytpted_2 = []
Binary = []
Binary1 = []
c_m_l = []
shift_amount = 0
n = 0
k = 3
j = 0
print("*********************\n","     Mission 00")
print("*********************\n")
print("--- hex of encrypted code ---")
print("-----------------------------\n")


def transformer(a):
    global Union
    temp = a
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


def to_int(bin):
    global n
    for y, b in enumerate(reversed(bin)):
        if b == '1':
            if y != (len(bin)-1):
                n += 2**y
            else:
                n -= 2**y
    return n


def hex2bin(num):
    bit = []
    if num == 0:
        return '0000'
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


for line in hurap_file.readlines():
    line = line.strip("\n")
    if not line.startswith("0" or "1"):
        continue
    else:
        Alien.append(line)


for i in Alien:
    contents = " "
    while len(contents) > 0:
        contents = i[j:k+1]
        transformer(contents)
        k += 4
        j += 4
    j = 0
    k = 3
    for index, eleman in enumerate(Union):
        for key,value in representations.items():
            if eleman == key:
                Union[index] = value
    secili = "".join(Union)
    Encrypted.append(secili)
    print(secili)
    Union.clear()
print("\n--- encrypted code ----")
print("-----------------------\n")
for ik in Encrypted:
    for sayi in range(0, len(ik), 2):
        for key, value in schucki.items():
            if ik[sayi:sayi+2] == value:
                Union.append(key)
    secili2 = "".join(Union)
    print(secili2)
    Dencrytpted.append(secili2)
    Union.clear()
print("\n--- decrypted code ---")
print("----------------------\n")

hurap_file.seek(0)
for line in hurap_file.readlines():
    if not line.startswith("0"or"1"):
        contents = " "
        line_list = list(line.strip())
        del line_list[0]
        secici3 = "".join(line_list)
        to_int(secici3)

def printer():
    global n
    global shift_amount
    shift_amount = n % len(alex)
    return shift_amount

printer()

def dict_roll(dct):
    sums = []
    schucki1 = collections.OrderedDict()
    shift_values = collections.deque(dct.keys())
    shift_values.rotate(n)
    for deger in shift_values:
        for value in dct.values():
            if value in sums:
                continue
            schucki1[deger] = value
            sums.append(value)
            break
    return schucki1


schucki1 = dict_roll(schucki)


for character in Encrypted:
    i = 0
    while len(character) > i:
        for key, value in schucki1.items():
            if character[i:i + 2] == value:
                Union.append(key)
                i += 2
    secici4 = "".join(Union)
    c_m_l.append(secici4)
    print(secici4)
    Union.clear()
    i = 0
print("\n*********************\n", "     Mission 01")
print("*********************\n")
for line in virus_codes_file.readlines():
    line = line.strip("\n").split(":")
    for line_s in line:
        substituted[line[0]] = line[1]
print(c_m_l)
print(substituted)

for line in c_m_l:
    for k1, v in substituted.items():
        if line.count(k1) != 0:
            u = len(k1)
            index = line.find(k1)
            t = line[index:u+index].replace(k1, v)
            virus = line.replace(k1, t, len(line))
            line = virus
    Encrypted_2.append(line)
    print(line)
print("\n*********************\n", "     Mission 10")
print("*********************")
print("\n--- encrypted code ----")
print("-----------------------\n")
for word in Encrypted_2:
    for enc in range(0, len(word)):
        for key, value in schucki1.items():
            if word[enc] == key:
                Union.append(value)
    secili6 = "".join(Union)
    Dencrytpted_2.append(secili6)
    Union.clear()

for letter in Dencrytpted_2:
    for dnc in range(0, len(letter), 2):
        for key, value in schucki.items():
            if letter[dnc:dnc+2] == value:
                Union.append(key)
    secili7 = "".join(Union)
    print(secili7)
    Binary.append(secili7)
    Union.clear()
print("\n--- hex of encrypted code ---")
print("-----------------------------\n")
for l in Dencrytpted_2:
    print(l)
print("\n--- bin of encrypted code ---")
print("-----------------------------")

for son in Dencrytpted_2:
    for last in son:
        for k2, value in representations.items():
            if last == value:
                secili8 = hex2bin(int(k2))
                Union.append(str(secili8))
                break
    print("".join(Union))
    Union.clear()

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()