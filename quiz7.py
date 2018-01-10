import sys
comparison = []
gamer = []
try:
    try:
        operand = sys.argv[1]
        operand_file = open(sys.argv[1], "r")
    except IOError:
            print("IOError: cannot open", sys.argv[1])
            print("\n~ Game Over ~")
    try:
        comparison__file = sys.argv[2]
        comparison_file = open(sys.argv[2], "r")
        for compare in comparison_file.readlines():
            compare = compare.strip("\n").split(" ")
            comparison.append(compare)
        for line in operand_file.readlines():
            gamer.clear()
            line = line.strip("\n").split(" ")
            print("------------")
            try:
                div = int(float(line[0]))
                nondiv = int(float(line[1]))
                From = int(float(line[2]))
                to = int(float(line[3]))
                for i in range(From, to + 1):
                    if i % div == 0 and i % nondiv != 0:
                        gamer.append(str(i))
                print("My results:\t\t", " ".join(gamer))
                print("Results to compare:\t", " ".join(comparison[0]))
                assert gamer == comparison[0], "ALEXDESOUZA"
            except ValueError:
                print("ValueError: only numeric input is accepted.")
                print("Given input:", " ".join(line))
            except IndexError:
                print("IndexError: number of operands less than expected.")
                print("Given input:", " ".join(line))
            except ZeroDivisionError:
                print("ZeroDivisionError: You can't divide by 0.")
                print("Given input:", " ".join(line))
            #except AssertionError:
             #   print("Assertion Error: results don't match.")
            except:
                print("kaBOOM: run for your life!")
            else:
                print("Goool!!!")
            finally:
                del comparison[0]
                comparison_file.close()
                operand_file.close()
    except IOError:
        print("IOError: cannot open", sys.argv[2])
except IndexError:
    print("IndexError: number of input files less than expected.")
finally:
    print("\n~ Game Over ~")
