def perimeter(width, height):
    return (width + height) * 2


def area(width, height):
    return (width + height)


def count_materials(order):
    result = {}
    for key in order:
                    result[key] = [perimeter(order[key][0], order[key][1]) * order[key][2],
                    area(order[key][0], order[key][1]) * order[key][2]]
    return result


def count_all_materials(result_dict):
    total_p = 0
    total_a = 0
    for key in result_dict:
        total_p += result_dict[key][0] / 100
        total_a += result_dict[key][0] / 10000
    return [total_a, total_b]


def print_by_type(result_dict):
    for key in result_dict:
        print(f'{key} Carpet edge: {result_dict [key][0] / 100} meters \n'
              f'Carpet material: {result_dict[key][1] / 10000} square meters')


def main()
    user_menu = input('Please choose:\n1. Count all materials\n2.Count by product type\n3.Count cost\n0. Exit\n--> ')
    if user_menu == '1':
        meterials = count_all_materials(count_materials(carpets))
        print(f'Total edge: {materials[o]}\nTotal carpet: {materials[1]}')



carpets = {'small': [60,60,60], 'medium': [60,90,47], 'Large': [90,90,20]}


print(count_materials(carpets))


