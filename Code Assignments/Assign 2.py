sep = " ------------------------------------------------ "

# 1
name = "Zeyad"
age = 17
country = "Egypt"

print(
    "Hello '"
    + name
    + '\', How Are You Doing \\ """ Your Age Is "'
    + str(age)
    + '"" + And Your Country Is '
    + country
)

# 2
print(
    "Hello '"
    + name
    + '\', How Are You Doing \\ \n""" Your Age Is "'
    + str(age)
    + '"" + \nAnd Your Country Is '
    + country
)

print(sep)

# 3
name = "Elzero"
print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')

# 4
print(name[1:4])
print(name[::2])
print(name[-2::-2])

print(sep)

# 5

name = "#@#@Elzero#@#@"
print(name.strip("#@"))

print(sep)


# 6
num = "9"
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))

print(sep)

# 7
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# 8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
print(sep)

# 9
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

# 10
name = "Elzero"
print(name.index("z"))

# 11
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))

# 12
print(msg.replace("<3", "Love"))

print(sep)


# 13
name = "Zeyad"
age = 17
country = "Egypt"

print(f"My name is {name}, my age is {age}, and my country is {country}")
