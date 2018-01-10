rj = [1,2,3,4,5,6,7,8,9,0,2,2,4,5,3,5]

#assert len(rj) == 15
if not len(rj) ==16:
    raise AssertionError()
else:
    print("got it")
#try:
assert 4 + 2 == 4,"Houston we've got a problem"
#except AssertionError:
 #   print("Houston we've got a problem")
#assert (2 + 2 = 5), "Houston we've got a problem"       # çalışmaz
#assert(2 + 2 == 5, "Houston we've got a problem")      # çalışmaz

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))

numSuccesses=12
numFailures=0
try:
    successFailureRatio = numSuccesses/numFailures
    print('The S/F ratio is', successFailureRatio)
except ZeroDivisionError as e:
    print('No failures, so the S/F is undefined.')
print('Now here')
i = True
while i == True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number', val**2)
        break #to exit the while loop
    except ValueError:
        print(val, 'is not an integer')
        i = False
print("done")


try:
    dividend = 5
    divisor = "sd" #0 da yaz sonra eğer aşşağıda type erroru yazmasam kendi error verip programı sonlandırır.
    division = dividend / divisor
except IOError:
    print("I can't open the file!")
except (ZeroDivisionError,ValueError) :#TypeError):    #eğer typeerroru açarsam aşşağıdaki exceptiona uğramaz yada exceptionu ıoerrorun önüne alırsam direk onun printini çıkartır diğerlerine uğramaz
    print("You can't divide by zero!")
except Exception as ValueError:                #Exception tüm erroları kapsar
   print("Exception occured and handled!")


try:
    dividend = 5
    divisor = "sd" #0 da yaz sonra eğer aşşağıda type erroru yazmasam kendi error verip programı sonlandırır.
    division = dividend / divisor

except IOError:
    print("I can't open the file!")
except (ZeroDivisionError,ValueError) :#TypeError):    #tek except tüm errorları içerir.Except exceptions keyboard ve system errorları içermez
    print("You can't divide by zero!")
except:
    print("Exception occured and handled!")

try:
    f = open('arg', 'r')
except IOError:
    print('cannot open', 'arg')
else:
    print('arg', 'has', len(f.readlines()), 'lines')      #If there is no exception, execute this block.

try:
    x = Hello + 20
    #x = 10 + 20
except:
    print ('I am in except block')
    x = 20 + 30
else:
    print ('I am in else block')
    x += 1
finally:
    print ('Finally x = %s' %(x))