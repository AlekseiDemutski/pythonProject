# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem < 5:
#         print(elem)
#

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = [elem for elem in a if elem in b]
# print(result)


# simp_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 1, 2, 3]
# simp_list.append('string')
# simp_list[2] = 77
# simp_list.append(['table', 'chair'])
# simp_list[3] = (22, 33, 44)
# print(simp_list[0])
# simp_list.remove('string')
# simp_list.count(1)
# print(simp_list.count(1))
# print(simp_list)

# simp_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 1, 2, 3]
# print(simp_list[0],simp_list[-1])

# a = 100
# b = 'string'
# a, b = b, a
# print(a)
# print(b)

# simp_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 1, 2, 3]
# lst = set(simp_list)
# # len(lst) == len(simp_list)
# print(len(lst))
# print(len(simp_list))


# dict = {1:'key1', 2: 777}
# dict['key2'] = 555
# dict[('tuple1', 'tuple2')] = ['this', 'is', 'a', 'list']
# item_by_key = dict[2]
# del_item = dict.pop(1)
# all_keys  = dict.keys()
# print(all_keys)

# print(item_by_key)
# print(dict)
# print(type(dict))



# set1 = {1, 2, 3, 4, 5}
# set_notch = frozenset({7, 8, 9, 'qw', 'as', 'zx'})
# print(set_notch)
# print(type(set_notch))
# print(set1)
# print(type(set1))
# set_un = set1 | set_notch
# print(set_un)
# intersection = set1 & set_notch
# print(intersection)
# print(type(intersection))


# def calc (a, b, operation):
#     result ='Operation is not supported'
#     if operation == '+':
#         result = a + b
#     elif operation == '-':
#         result = a - b
#     elif operation == '*':
#         result = a * b
#     elif operation == '/':
#         result = a / b
#         if b != 0:
#             result = a / b
#         else:
#             result = 'not possible to /o'
#     return result
#
#
#
# if __name__ == '__main__':
#     print(calc(30, 15, '+'))
#     print(calc(30, 15, '-'))
#     print(calc(30, 15, '*'))
#     print(calc(30, 15, '/'))
#     print(calc(30, 0, '+'))
#     print(calc(30, 15, '%'))

# def even (num):
#     return num % 2 == 0
#
# # if __name__ == '__main__':
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 12, 34, 45 ,67 ,78 ,89]
# for item in lst:
#     if item == 139:
#         break
#     if not even(item):
#         print(item)
#

# lst = []
# for item in range(18, 1, -4):
#     lst.append(item)
#
# print(lst)

# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# sm = 0
# for item in lst:
#     if (item < 30) and (item % 3 == 0):
#         print(item, ' is ok')
#     else:
#         sm += item
# print('Sum: ', sm)

def month_season (month):
    season_ranges = {
        (12, 1, 2): 'Winter',
        (3, 4, 5): 'Spring',
        (6, 7, 8): 'Summer',
        (9, 10, 11): 'Autumn'
    }
    season = None

    for key, value in season_ranges.items():
        if month in key:
            season = value
            break
    return season

print(month_season(10))
print(month_season(5))
print(month_season(8))
print(month_season(9))
print(month_season(12))
print(month_season(999))

# str1 = ('Сидел барсук в своей норе и ел картошечку пюре')
# str1 = str1 + '.'
# if 'ре' in str1:
#     print(True)
# print(str1)
# print(len(str1))
# print(type(str1))
# print(str1.count('ре'))
# print(str1[-2])
# print(str1[1::2])
# print(str1.count(' ') + 1)


# my_string = ('пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.')
# my_string = my_string.capitalize()
# my_string = my_string.replace('сопровождать', 'поддерживать')
#
# print(my_string)
#
# my_string = my_string.split(',')
# my_string = ','.join(my_string)
# print(my_string)
# print(my_string.find('сопровождать'))
# print(my_string.index('сопровождать'))


# num = 12345
#
# def sum_for(num):
#     s = 0
#     for item in str(num):
#         s = s + int(item)
#     return s
#
#
# def sum_list(num):
#     lst = [int(item) for item in str(num)]
#     return sum(lst)
#
# print(sum_for(num))
# print(sum_list(num))


# string_x = '01101011101011'
#
# print(string_x.replace('1', '0', 1))
# print(string_x.replace('1', '0', 5))
# print(string_x.replace('1', '0'))
# print(string_x.replace('1', '0', 9))
# print(string_x.replace('1', '0', 10))


# string_y = input('Inset your word: ').lower().replace(' ', '').replace('.', '').replace(',', '')
# string_poly = string_y[::-1]
# if string_y == string_poly:
#     print('Your string is palindrome')
# else:
#     print('Your string is NOT palindrome')
#
# print(string_y)
# print(string_poly)


# def swap_words(string_z):
#     lst = string_z.split(' ')
#     lst.reverse()
#
#     return ' '.join(lst)
#
# print(swap_words('good day'))










