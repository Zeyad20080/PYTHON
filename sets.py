# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour)


# -----------------
# -- Set Methods --
# -----------------

a = {1, 2, 3}
a.clear()
print(a)

b = {1, 2, 3}
c = {2, 3, 4, 5}
x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6}
print(b | c)  # Union
print(b.union(c))  # Union
x.union_update(y)  # Union Update
print(x)  # x is now {1, 2, 3, 4, 5, 6}


print(b & c)  # Intersection
print(b.intersection(c))  # Intersection
x.intersection_update(y)  # Intersection Update
print(x)  # x is now {3, 4, 5}

print(b - c)  # Difference
print(b.difference(c))  # Difference
x.difference_update(y)  # Difference Update
print(x)  # x is now {1, 2}

print(b ^ c)  # Symmetric Difference
print(b.symmetric_difference(c))  # Symmetric Difference
x.symmetric_difference_update(y)  # Symmetric Difference Update
print(x)  # x is now {1, 2, 6}


d = {1, 2, 3}
d.add(5)  # Add an item
print(d)

e = d.copy()  # Copy the set

d.remove(3)  # Remove an item
# d.remove(10)  # Raises KeyError if 10 is not in the set
print(d)

e.discard(2)  # Discard an item, no error if not found
print(e)
e.discard(10)  # No error, even if 10 is not in the set


f = {1, 2, 3}
f.pop()  # Removes and returns an arbitrary item
print(f)

g = {1, 2, 3}
g.update({4, 5})  # Add multiple items
print(g)


# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True
