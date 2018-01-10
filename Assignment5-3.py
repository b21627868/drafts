import sys
s_file = open(sys.argv[1], "r", encoding="utf8")
searching_name = sys.argv[2]
names = []
dic = {}
print("Searching value is:", searching_name, "\n")
fill_in_the_blanks = open("output.txt", "w")
for line in s_file.readlines():
    line = line.strip().split(":")
    names.append(line[0])
    dic[line[0]] = line[1]


def writer(List):
    for name in List:
        if name == List[-1]:
            print(name)
        else:
            print(name, end=" ")


def sorting(names):
    for i in range(len(names)):
        for j in range(0, len(names)-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names


writer(names)
sorting(names)


def recurs(student):
    writer(student)
    fill = " ".join(student)
    fill_in_the_blanks.write(fill)
    fill_in_the_blanks.write("\n")
    middle = student[(len(student)-1) // 2]
    index = (len(student)-1) // 2
    if len(student) == 1:
        if searching_name == student[0]:
            print("The search string is ", searching_name, "and the city is", dic.get(searching_name))
        else:
            print("The search string was not found in file")
        return
    else:
        if searching_name < middle:
            return recurs(student[:index])
        elif searching_name == middle:
            print(searching_name)
            print("The search string is ", searching_name, "and the city is", dic.get(searching_name))
        else:
            return recurs(student[index+1:])


recurs(names)
fill_in_the_blanks.close()
