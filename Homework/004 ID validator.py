while True:
    try:
        user_input = input('Please enter your ID: ')
        if user_input.lower() == 'exit':
            break
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
        print('ID you entered is not 11 digits long')
        continue
    else:
        if user_input[0] == '1':
            birth_century = '19'
            gender = 'Man'
        elif user_input[0] == '2':
            birth_century = '19'
            gender = 'Woman'
        elif user_input[0] == '3':
            birth_century = '20'
            gender = 'Man'
        elif user_input[0] == '4':
            birth_century = '20'
            gender = 'Woman'
        elif user_input[0] == '5':
            birth_century = '21'
            gender = 'Man'
        elif user_input[0] == '6':
            birth_century = '21'
            gender = 'Woman'
        else:
            birth_century = 'Unknown'
            gender = 'Unknown'

        byear = user_input[1:3]
        bmonth = user_input[3:5]
        bday = user_input[5:7]

        if int(user_input) in range(1, 11):
            bregion = 'Kuressaare haigla'
        elif int(user_input) in range(11, 20):
            bregion = 'Tartu Ülikooli Naistekliinik'
        elif int(user_input) in range (21, 151):
            bregion = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif int(user_input) in range(151, 161):
            bregion = 'Keila haigla'
        elif int(user_input) in range(161, 221):
            bregion = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif int(user_input) in range(221, 271):
            bregion = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif int(user_input) in range (271, 371):
            bregion = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
        elif int(user_input) in range(371, 421):
            bregion = ' Narva haigla'
        elif int(user_input) in range(421, 471):
            bregion = 'Pärnu haigla'
        elif int(user_input) in range(471, 491):
            bregion = 'Haapsalu haigla'
        elif int(user_input) in range(491, 521):
            bregion = 'Järvamaa haigla (Paide)'
        elif int(user_input) in range(521, 571):
            bregion = 'Rakvere haigla, Tapa haigla'
        elif int(user_input) in range(571, 601):
            bregion = 'Valga haigla'
        elif int(user_input) in range(601, 651):
            bregion = 'Viljandi haigla'
        elif int(user_input) in range(651, 701):
            bregion = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
        else:
            bregion = 'You were not born in Estonia'

        while True:
            user_choice = input('Please insert following number to see:\n'
                                '1. Users gender\n'
                                '2. Users date of birth\n'
                                '3. Users place of birth\n'
                                '4. Validate ID\n'
                                '5. Change ID\n'
                                '7. Exit\n'
                                '->->->')
            if user_choice == '1':
                if gender != 'Unknown':
                    print(f'Gender is: {gender}')
                else:
                    print('Impossible to determinate gender')
            elif user_choice == '2':
                if birth_century != 'Unknown':
                    print(f'Date of birth {bday}.{bmonth}.{byear}')
                else:
                    print('Impossible to determine date of birth.')
            elif user_choice == '3':
                if bregion != 'You were not born in Estonia':
                    print(f'Your region of birth is {bregion}')
                else:
                    print('You were not born in Estonia')
            elif user_choice == '4':
                check_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                check_list2 = [3, 4, 5, 6, 7, 8 ,9, 1, 2, 3]

                result = 0
                index = 0
                for num in check_list1:
                    result += num * int(user_input[index])
                    index += 1
                if result % 11 == int(user_input[10]):
                    print('ID is valid')
                else:
                    result = 0
                    index = 0
                    for num in check_list2:
                        result += num * int(user_input[index])
                        index += 10
                    if result % 11 == int(user_input[10]):
                        print('Id is valid')
                    else:
                        print('ID is not valid')

            elif user_choice == '5':
                break
            elif user_choice == '7':
                print('See you next time!')
                quit()
            else:
                print("Something's Gone Wrong")




