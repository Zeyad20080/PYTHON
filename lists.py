# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myList = ["Zeyad", "Ahmed", "Osama"]

myList[0:1] = [10]
print(myList)


# -------------------
# -- Lists Methods --
# -------------------

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

print(myFriends.append("Zeyad"))  # append: Adds an item to the end of the list
print(myFriends.append(myOldFriends))  # append: Adds a *list* to the end of the list
print(
    myFriends.extend(myOldFriends)
)  # extend: Adds *items* of a list to the end of the list

print(
    myFriends.count("Ahmed")
)  # count: Returns the number of times an item appears in the list
print(
    myFriends.index("Ahmed")
)  # index: Returns the index of the first occurrence of an item
print(
    myFriends.index("Ahmed", 0, 2)
)  # index: Returns the index of the first occurrence of an item within a specified range
print(myFriends.insert(0, "Mohamed"))  # insert: Adds an item at a specific index
print(myFriends.remove("Ahmed"))  # remove: Removes the first occurrence of an item
print(myFriends.pop())  # pop: Removes the last item and returns it
print(myFriends.pop(0))  # pop: Removes the item at a specific index and returns it
print(myFriends.clear())  # clear: Removes all items from the list

print(myFriends.sort())  # sort: Sorts the list in ascending order
print(myFriends.reverse())  # reverse: Reverses the order of the list

newlist = myFriends.copy()  # copy: Creates a shallow copy of the list
