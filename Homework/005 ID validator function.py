def input_check():
    global user_input
    while True:
        user_input = input('Please enter your ID: ')
        try:
            if user_input.lower() == 'exit':
                print('Good bye')
                quit()
            int(user_input)
            if len(user_input) != 11:
                if len(user_input) > 11:
                    print('ID is too long! ')
                else:
                    print('ID is too short')
                raise UserWarning
        except ValueError:
            print('ID you entered is not numeric!')
        except UserWarning:
            print('ID you entered is not 11 digits long!')
        else:
            break


def user_gender():
    global user_input
    if user_input[0] == '1':
        gender = 'Man'
    elif user_input[0] == '2':
        gender = 'Woman'
    elif user_input[0] == '3':
        gender = 'Man'
    elif user_input[0] == '4':
        gender = 'Woman'
    elif user_input[0] == '5':
        gender = 'Man'
    elif user_input[0] == '6':
        gender = 'Woman'
    else:
        gender = 'Unknown'
    return gender


def dob():
    global user_input
    byear = user_input[1:3]
    bmonth = user_input[3:5]
    bday = user_input[5:7]
    return (f'Date of birth {bday}.{bmonth}.{byear}')


def region():
    global user_input
    if int(user_input[7:10]) in range(1, 11):
        bregion = 'Kuressaare haigla'
    elif int(user_input[7:10]) in range(11, 20):
        bregion = 'Tartu Ülikooli Naistekliinik'
    elif int(user_input[7:10]) in range(21, 151):
        bregion = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(user_input[7:10]) in range(151, 161):
        bregion = 'Keila haigla'
    elif int(user_input[7:10]) in range(161, 221):
        bregion = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(user_input[7:10]) in range(221, 271):
        bregion = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(user_input[7:10]) in range(271, 371):
        bregion = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(user_input[7:10]) in range(371, 421):
        bregion = ' Narva haigla'
    elif int(user_input[7:10]) in range(421, 471):
        bregion = 'Pärnu haigla'
    elif int(user_input[7:10]) in range(471, 491):
        bregion = 'Haapsalu haigla'
    elif int(user_input[7:10]) in range(491, 521):
        bregion = 'Järvamaa haigla (Paide)'
    elif int(user_input[7:10]) in range(521, 571):
        bregion = 'Rakvere haigla, Tapa haigla'
    elif int(user_input[7:10]) in range(571, 601):
        bregion = 'Valga haigla'
    elif int(user_input[7:10]) in range(601, 651):
        bregion = 'Viljandi haigla'
    elif int(user_input[7:10]) in range(651, 701):
        bregion = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        bregion = 'You were not born in Estonia'
    return (bregion)


def validate():
    global user_input
    check_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    check_list2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    index = 0
    for num in check_list1:
        result += num * int(user_input[index])
        index += 1
    if result % 11 == int(user_input[10]):
        return ('ID is valid')
    else:
        result = 0
        index = 0
        for num in check_list2:
            result += num * int(user_input[index])
            index += 1
        if result % 11 == int(user_input[10]):
            return ('Id is valid')
        else:
            return ('ID is not valid')


def user_menu():
    while True:
        user_choice = input('Please insert following number to see:\n'
                            '1. Users gender\n'
                            '2. Users date of birth\n'
                            '3. Users place of birth\n'
                            '4. Validate ID\n'
                            '5. Change ID\n'
                            '0. Exit\n'
                            '->->-> ')
        if user_choice == '1':
            if user_gender != 'Unknown':
                print(user_gender())
        elif user_choice == '2':
            print(dob())
        elif user_choice == '3':
            print(region())
        elif user_choice == '4':
            print(validate())
        elif user_choice == '5':
            input_check()
        elif user_choice == '0':
            print('Have a nice day!')
            exit()
        else:
            print('Value is out of range. Try again.')


user_input = ''
input_check()
user_menu()
user_gender()
dob()
region()
validate()

