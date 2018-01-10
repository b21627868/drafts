assert 2> 5   # 6 yerine 2 koy
number = int(input('Enter a positive number:'))
assert number > 0, 'Only positive numbers are allowed!'

def chkassert(num):
    assert type(num) == int


#chkassert("a")

def getUser(self, id, Email):

    user_key = id and id or Email
    print(user_key)
    assert user_key

getUser("burak04","","12")

x = "burak" or "yılmaz" # and ile yazınca yılmaz çıkıyo
print(x)
this_is_very_complex_function_result = 9
c = this_is_very_complex_function_result
test_us = (c < 4)
if test_us == True:
    print("YES! I am right!")
else:
    print("I am Wrong, but the program still RUNS!")
assert test_us,"burda hata verdi"      #normalde hata vermiyo assertsiz çalıştırınca ancak assertli çalıştırınca yaptığı şey test etmek eğer tes_us 4 den küçükse sıkıntı yok eğer değilse assert hatayı bulur ve istenilen hatayı yazar
