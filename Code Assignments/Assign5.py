# 1
myTuple = ("Zeyad",)
print(myTuple[0])
print(type(myTuple))

# 2
friends = ("Zeyad", "Youssef", "Osama")
friends = list(friends)
friends[0] = "Ahmed"
friends = tuple(friends)
print(friends)
print(type(friends))
print(len(friends))

# 3
nums = (1, 2, 3)
letters = ("A", "B", "C")

nums_and_letters = nums + letters
print(nums_and_letters)
print(len(nums_and_letters))

# 4
myTuple = (1, 2, 3, 4)
a, b, _, c = myTuple

print(a, b, c, sep="\n")
