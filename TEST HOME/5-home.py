t1 = (1, 2, 3, 5, 8)
t2 = (8, 2, 5)


t1 = list(t1)

t1[2:2] = t2
t1 = tuple(t1)

print(t1)

