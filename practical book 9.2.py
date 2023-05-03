'''
    if n%3 == 0:
        return 'Fizz'
    elif n%5 == 0:
        return 'Buzz'
    elif n%3 == 0 and n%5 == 0:
        return 'FizzBuzz'
    else:
        return n'''

for i in range (1, 101) :
    if i % 3 == 0 :
        print ("Fizz")
    if i % 5 == 0 :
        print ("Buzz")
    if i % 3 == 0 and i % 5 == 0 :
        print ("Fizz Buzz")
