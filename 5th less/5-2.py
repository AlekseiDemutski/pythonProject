condition = True
while condition:
    user_choise = input("Please choose:\n1.Print 'Hello world'\n2.Print 'Hello planet\n"
                        "3.Exit\n--> ")

    if user_choise == '1':
        print("Hello world")
    elif user_choise == '2':
        print('Hello planet')
    elif user_choise == '3':
        quit()
    elif user_choise == '4':
        x = 100
        while x > 0:
            print(x)
            x -= 1
    else:
        print('Choise is out of range')

print("Good bye")

x = 0
while x < 101:
        if x % 5 == 0 and x % 3 == 0:
            print(x, 'FizzBuzz')
        elif x % 3 == 0:
            print(x, 'Fizz')
        elif x % 5 == 0:
            print(x, 'Buzz')
        x += 1


# distance_to_target = float(input('lPlease enter distance in km'))
# current_position = 0
#
# step = 0.6
# step_ctn = 0
# distance_in_meters = distance_to_target * 1000
#
# while current_position < distance_in_meters:
#     if step_ctn % 1000 == 0:
#         print(step_cnt)
#     current_position += step
#     step_ctn += 1
# print('Steps to walk')


