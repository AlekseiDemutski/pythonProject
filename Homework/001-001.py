years
current_year = int(input('current_year '))
year_of_birth = int(input('year_of_birth '))

age = (current_year - year_of_birth)

print(' Your age is', age)

# code 2 data
x = 152
y = 132

Result_a = (x / y)-int(x / y)
print('Result a. equals  ', Result_a)

Result_b = Result_a * 13
print('Result b. equals', Result_b)

Result_c = (Result_b)**0.5
print('Result c. equals', Result_c)

Result_d = int(Result_c)
print('Result d. equals', Result_d)


# 3. Соединить код в отдельную переменную
# 	    пример:
# 475 - 12 - 967


code_1 = input('code 1 ')
code_2 = input('code 2 ')
code_3 = input('code 3 ')

Secret_code = (str(code_1) + ' - ' + str(code_2) + ' - ' + str(code_3))
print('Secret code is ', Secret_code)

code_1 = input('code 1 ')
code_2 = input('code 2 ')
code_3 = input('code 3 ')

print('Your secret code is', code_1, ' - ', code_2, ' - ', code_3)


# 4. Вывести строку:
# 		пример:
# 			Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.


first_name = input('Insert your First Name ')
last_name = input('Insert your Last Name ')
age = input('Insert your age ')

code_1 = input('Insert code 1 ')
code_2 = input('Insert code 2 ')
code_3 = input('Insert code 3 ')

print('Hello', first_name, last_name + '. You are', age,'years old. Your secret code is',code_1 + '-' + code_2 + '-' + code_3)

print('Hello ' + first_name + ' ' + last_name + '. You are ' + age +
      ' years old. Your secret code is ' + code_1 + '-' + code_2 + '-' + code_3 + '.')

















































