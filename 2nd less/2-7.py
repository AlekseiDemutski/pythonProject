
A = float(input('Enter side A: '))
B = float(input('Enter side B: '))
C = float(input('Enter side C: '))

half_perimeter = (A + B + C) / 2
triangle_area = (half_perimeter * (half_perimeter - A) * (half_perimeter - B) * (half_perimeter - C))**0.5
print('Area of triangle is', triangle_area)











