def to_int(bin): # from definition
    n = 0
    for i, b in enumerate(reversed(bin)):
        print(i,b)
        if b == '1':
           if i != (len(bin)-1):
              n += 2**i
           else: # MSB
              n -= 2**i
    return n


print(to_int('1111110100101'))
def bin2dec(b):
    number = 0
    counter = 0
    for t in b[::-1]: # Iterating through b in reverse order
        number += int(t)*(2**counter)
        counter += 1

    return number