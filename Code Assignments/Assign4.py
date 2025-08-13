# 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]


print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

# 2
print(friends[0::2])
print(friends[1::2])

# 3
print(friends[1:4])
print(friends[-2:])

# 4
friends[-2:] = ["Elzero", "Elzero"]
print(friends)

# 5
friends.insert(0, "Zeyad")
print(friends)
friends.append("Mo")
print(friends)

# 6
friends.pop(0)
friends.pop(0)
print(friends)
friends.pop()
print(friends)


# 7
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# 8
print(len(friends))


# 9
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])
