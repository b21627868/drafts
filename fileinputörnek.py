import sys
import fileinput
in_file_by = sys.argv[1]
out_file_by = sys.argv[2]
by_in = open(in_file_by ,"r")
by_out = open(out_file_by, "w")
#print(len(by_in.readlines()))
lines = []
def sort_file():
    global lines
    for line in fileinput.input(sys.argv[1]):
        #print(line)
        lines.append(line.rstrip())
        #print(lines)
        lines.sort()
    for line in lines:
        print(line)
       #by_out.write(line)
    return lines


sort_file()

