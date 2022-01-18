string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = "* extra whitespace string *"
german_sample = "der Fluẞ"

print(string_sample.lower())
print(string_sample.casefold())
print(string_sample[5:12].upper())
print(string_sample2.capitalize())
print(string_sample3.strip('* '))
print(string_sample3.rstrip('* '))

print(string_sample.replace("world", '').replace('','').upper())

a, b, c = string_sample.split()
print(string_sample.split())

print(a)
print(b)
print(c)

a, b, c = input("Please enter something").split()

print(a)
print(b)
print(c)






