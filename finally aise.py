def gb():
    x = 5
    try:
        x +=4
    except:
        print("yeter")
    finally:
        x=x+5

    return x
print(gb())

try:
    y =5
    #y +="asd"
    x = 3
    try:
        #x =x/0                                               #lecture 8 examples im bbm101
        #print(t)
        y +="vbn"
    except TypeError:   #exception1
        print("exception1 error")
        print(u)
    except NameError: #exception2
        print("exception2 error")
    try:
        y*"asdasdas"
    except (ZeroDivisionError,TypeError,NameError):   #exception3
        print("exception3 error+++")
    x=x/0
except (ZeroDivisionError,TypeError,NameError):    #exception3
    print("exception3 error",end="   ")
    print("adam")
print("hello")

def getRatios(vect1, vect2):
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise IndentationError('getRatios called with bad arguments')
    return ratios
try:
    print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0]))
except IndentationError as msg:
    print(msg)


def demo_bad_catch():
    try:
        raise ValueError('a hidden bug, do not catch this')
        raise Exception('This is the exception you expect to handle')
    except Exception as himmi:
        print('caught this error: ' + repr(himmi))

demo_bad_catch()

#def demo_no_catch():
#    try:
 #       raise Exception('general exceptions not caught by specific handling')
  #  except ValueError as e:
   #     print('we will not catch e')

#print(demo_no_catch())
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass
number = 10
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
                raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")