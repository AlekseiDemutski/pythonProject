num = range(1, 101)
for number in num:
    if number % 3 == 0:
        print(number, 'Fizz')
    if number % 5 == 0:
        print(number, 'Buzz')
    if number % 3 and number % 5 == 0:
        print(number, 'FizzBuzz')
    else:
        print(number, False)



