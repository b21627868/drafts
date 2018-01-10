import sys
from operator import itemgetter
import collections
dic = collections.OrderedDict()
garbage, sort, edition, dvd1, dvd2, union, go_ahead_eagles, key = [], [], [], [], [], [], [], []
dvd, final_edition, mbappe = [], [], []
name, genre, director, state = [], [], [], []
mission = ["A", "H", "Q", "R", "S", "L", "E"]
try:
    dvd_file = open(sys.argv[1], "r+", encoding="utf8")
    for line in dvd_file.readlines():
        line = line.strip("\n").split(";")
        del line[-1]
        dvd.append(line)
except:
    dvd_file = open("dvdStore.txt", "w", encoding="utf8")
    print("Warning: Your file is empty don't use H,R,S,L,E commands")

def menu():
    print("---HUBM DVD---")
    print("A: Add new dvd")
    print("R: Remove dvd")
    print("S: Search dvd")
    print("L: List dvd")
    print("E: Edit dvd")
    print("H: Hire dvd")
    print("Q: Quit")


menu()
for i in range(len(dvd)):
    for k in dvd:
        try:
            secici = k[i].split(",")
            for p in secici:
                p = p.strip()
                union.append(p)
            secici1 = ",".join(union)
            dvd1.append(secici1)
            union.clear()
        except:
            pass

def whitespace(lister):
    global final_edition, go_ahead_eagles
    for roda in lister:
        roda = roda.strip()
        final_edition.append(roda)
    go_ahead_eagles.clear()
    for score in final_edition:
        go_ahead_eagles.append(score)
    final_edition.clear()


for i in dvd1:
    i = i.split(",")
    dvd2.append(i)
def warning():
    print("hello")

def writer(dic):
    for write, write1 in dic.items():
        output.write(write)
        output.write(",")
        write1 = ",".join(write1)
        output.write(write1)
        output.write("\n")


def writer2(dictionary):
    for write, write1 in dic.items():
        dvd_file.write(write)
        dvd_file.write(",")
        write1 = ",".join(write1)
        dvd_file.write(write1)
        dvd_file.write(";")
        dvd_file.write("\n")


def diccer(list):
    global dvd2
    for cd in list:
        dic[cd[0]] = cd[1:]


def quotes(another_list):
    global go_ahead_eagles
    for ajax in another_list:
        try:
            ajax = ajax.replace('"', "", len(ajax))
            go_ahead_eagles.append(ajax)
        except:
            pass


diccer(dvd2)
commands = " "


def commands_user():
    global commands
    commands = input("Enter command:").split(",")
    return commands


while commands[0] != "Q":
    commands_user()
    if commands[0] == "Q":
        break
    if commands[0] == "A":
        if dic.get(commands[1]) != None:
            print("Serial number already in use")
        else:
            if type(int(commands[2])) != int:
                print("Price must be integer or float")
            else:
                quotes(commands)
                whitespace(go_ahead_eagles)
                go_ahead_eagles.append("Inv")
                dic[go_ahead_eagles[1]] = go_ahead_eagles[2:]
                dvd2.append(go_ahead_eagles)
                go_ahead_eagles.clear()
    if commands[0] == "R":
        if len(dic) == 0:
            print("File is empty there is nothing to remove")
        if len(dic) != 0:
            print(dic.get(commands[1]))
            answer = input("Do you want to confirm the deletion? Yes or No?")
            delete = dic.get(commands[1])
            if delete[-1] == "Hired":
                print("You can not delete this item because it was hired")
            else:
                del dic[commands[1]]
            writer(dic)
    if commands[0] == "S":
        quotes(commands)
        whitespace(go_ahead_eagles)
        if len(dic) == 0:
            print("File is empty you can't search anything")
        if len(dic) != 0:
            if len(go_ahead_eagles[1]) >= 3:
                for keyy, value in dic.items():
                    changing = "".join(value)
                    if go_ahead_eagles[1] in changing:
                        mbappe.append(changing)
                        print("Serial:", end="   ")
                        print(keyy)
                        for number in range(len(value)):
                            if number == 0:
                                print("Price:", end="    ")
                                print(value[0])
                            if number == 1:
                                print("Name:", end="     ")
                                print(value[1])
                            if number == 2:
                                print("Genre:", end="    ")
                                print(value[2])
                            if number == 3:
                                print("Director:", end=" ")
                                print(value[3])
                            if number == 4:
                                print("State:", end="    ")
                                print(value[4])
                                print("-------------------")
                if len(mbappe) == 0:
                    print("Searching value cannot be found")
            else:
                print("At least you must enter 3 letter")
            go_ahead_eagles.clear()
            mbappe.clear()
    if commands[0] == "L":
        if len(dic) == 0:
            print("File is empty there is nothing to list")
        if len(dic) != 0:
            for k, v in dic.items():
                name.append(v[1])
                genre.append(v[2])
                director.append(v[3])
                state.append(v[4])
                sort.append(v)
                key.append(int(k))
            name_1 = max(name, key=len)
            genre_2 = max(genre, key=len)
            director_2 = max(director, key=len)
            state_2 = max(state, key=len)
            new = sorted(sort, key=itemgetter(1))
            print("Serial".ljust(6), "Price".ljust(6), "Name".ljust(len(name_1)+2), "Genre".ljust(len(genre_2)), "Director".ljust(len(director_2)), "State".ljust(len(state_2)))
            print("------".ljust(6), "-----".ljust(6), "----".ljust(len(name_1)+2), "-----".ljust(len(genre_2)), "--------".ljust(len(director_2)), "-----".ljust(len(state_2)))
            print(str(key[0]).ljust(7), end="")
            az = 1
            for p in new[0]:
                if az == 1:
                    temp = 7
                if az == 2:
                    temp = len(name_1)+3
                if az == 3:
                    temp = len(genre_2)+1
                if az == 4:
                    temp = len(director_2)+1
                if az == 5:
                    temp = len(state_2)
                print(p.ljust(temp), end="")
                az += 1
            az = 1
            i = 1
            try:
               while True:
                input()
                if i != len(new):
                    print(str(key[i]).ljust(7), end="")
                for u in new[i]:
                    if az == 1:
                        temp = 7
                    if az == 2:
                        temp = len(name_1)+3
                    if az == 3:
                        temp = len(genre_2)+1
                    if az == 4:
                        temp = len(director_2)+1
                    if az == 5:
                        temp = len(state_2)
                    print(u.ljust(temp), end="")
                    az += 1
                az = 1
                i += 1
            except IndexError:
                print("Dvd content is empty")
            mbappe.clear()
            new.clear()
            sort.clear(), state.clear(), genre.clear(), director.clear(), name.clear()
    if commands[0] == "E":
        if len(dic) == 0:
            print("File is empty you can not edit any dvd")
        if len(dic) != 0:
            try:
                for i in range(2, len(commands)):
                    edit = commands[i].split("=")
                    if edit[0][1:5] == "Name" or edit[0] == "name":
                        change = dic.get(commands[1])
                        change[1] = edit[1][1:-2]
                    if edit[0][1:7] == "Price" or edit[0] == "price":
                        change = dic.get(commands[1])
                        change[0] = edit[1][:-1]
                    if edit[0][1:6] == "Genre" or edit[0] == "genre":
                        change = dic.get(commands[1])
                        change[2] = edit[1][1:-2]
                    if edit[0][1:9] == "Director" or edit[0] == "director":
                        change = dic.get(commands[1])
                        change[3] = edit[1][1:-2]
            except:
                print("Serial key for editing couldn'find")
    if commands[0] == "H":
        if len(dic) == 0:
            print("File is empty you can not hire a dvd")
        else:
            if len(dic) != 0:
                try:
                    change = dic.get(commands[1])
                    change23 = ",".join(change)
                    print(commands[1], end=",")
                    print(change23)
                    if change[-1] == "Hired":
                        print("Selected dvd already hired")
                    else:
                        change[-1] = "Hired"
                        print("You hired the selected dvd")
                except:
                    print("Searching value couldn't find")
    if commands[0] not in mission:
        print("You wrote unsuitable command try again:")
    menu()
if commands[0] == "Q":
    if len(dic) == 0:
            print("There is nothing to show try to some add dvds")
    output = open("dvdStore.txt", "w")
    for k, v in dic.items():
        printer1 = ",".join(v)
        printer = k+","+printer1+";"
        print(printer)
    writer(dic)
    dvd_file.seek(0)
    writer2(dic)
    output.close()
    dvd_file.close()