grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())

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
Alien = []
for i in schuckscii_file.read().splitlines():
    print(i)

for line in hurap_file.read().split():
    print(line)
    if not line.startswith("0" or "1"):
        continue
    else:
        Alien.append(line)

print(Alien)