# x = [1, 2, 3]
# try:
#     # int('123234345')
#     print(x[10])
# except ValueError:
#     print('ERROR')
# except IndexError:
#     print('Index ERROR')
# else:
#     print('OK')
# finally:
#     print('Good bye')



while True:
    try:
        user_input = input('Pleaee enter your ID (type exit to quit: ')
        if user_input.lower() == 'exit':
            break
        int(user_input)

        if len(user_input) != 11:
            if len(user_input) > 11:
                print('Id is too long')
            else:
                print("ID is too short")
            raise UserWarning
    except ValueError:
        print('ID you entered is not numeric')
    except UserWarning:
        print('Id yu entered is not 11 digits long')
    else:
        print(user_input)
        break
