people = [
    ('Jack', 'Smith', 25, 'Male'),
    ('Mary', 'Gold', 18, 'Female'),
    ('Sarah', 'Connor', 32, 'Female'),
    ('Pierre', 'Summers', 45, None)
]

# for person in people:
#     if person[3] == 'Male':
#         print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')
#     elif person[3] == 'Female':
#         print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')

# for name, surname, age, gender, in people:
#     if gender == 'Male':
#         print(f'This is {name} {surname}. He is {age} years old.')
#     elif gender == 'Female':
#         print(f'This is {name} {surname}. She is {age} years old.')
#     else:
#         print(f'This is {name} {surname}. It is {age} years old.')


numbers = [1, 2, 3, 4, 5]
numbers2 = []
for num in numbers:
    numbers2.append(num ** 2)

print(numbers2)






# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# x = range(0, 101)
# for num1 in range(1, 4):
#     for num2 in range(1, 4):
#         for num3 in range(1, 4):
#             for num4 in range(1, 4):
#                 print(num1, num2, num3, num4)



# sample_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# for i, v, c in sample_list:
#     print(i)
#     print(v)
#     print(c)

# print(list(enumerate(sample_list, start=1)))