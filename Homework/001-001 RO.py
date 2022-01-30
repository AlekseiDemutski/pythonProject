first_name = input('Insert your first name ')
last_name = input('Insert your last name ')
current_year = int(input('Insert current year '))
year_of_birth = int(input('Insert year of birth '))

age = (current_year - year_of_birth)
# print(age)

# code 2 data
x = 152
y = 132

code_2 = int((x % y * 13) ** 0.5)
# print(code_2)

# code parts
code_1 = '354'
code_3 = 132

secret_code = str(code_1) + '-' + str(code_2) + '-' + str(code_3)
secret_code = f'{code_1}-{code_2}-{code_3}' #второй и лучший способ
print(secret_code)

print('Hello', first_name, last_name + '. You are', age, 'years old. Your secret code is', secret_code + '.')
print(f'Hello {first_name} {last_name}. You are {current_year - year_of_birth} years old.'
      f' Your secret code is {secret_code}.') #Второй и лучший способ






