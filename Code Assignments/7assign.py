# 1
print(True)
print(100 > 20)
print(150 == 150)
print(bool("Zoz"))

print(False)
print(100 < 20)
print(150 != 150)
print(bool(""))
print(bool(0))
print("*" * 50)

# 2
html = 80
css = 60
javascript = 70


print(html > 50 and css > 50 and javascript > 50)  # True

print("*" * 50)

# 3
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("*" * 50)
# 4
num_one = 10
num_two = 20

result = num_one + num_two
print(result)

print(result**3)
print(result**3 % 26000)
print((result**3 % 26000) / 5)
print(type(str((result**3 % 26000) / 5)))
