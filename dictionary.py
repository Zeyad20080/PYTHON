# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5,
}

print(user)
print(user["country"])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
    "One": {"name": "Html", "progress": "80%"},
    "Two": {"name": "Css", "progress": "90%"},
    "Three": {"name": "Js", "progress": "90%"},
}

print(languages)
print(languages["One"])
print(languages["Three"]["name"])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {"name": "Vuejs", "progress": "80%"}

frameworkTwo = {"name": "ReactJs", "progress": "80%"}

frameworkThree = {"name": "Angular", "progress": "80%"}

allFramework = {"one": frameworkOne, "two": frameworkTwo, "three": frameworkThree}

print(allFramework)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {"name": "Osama"}
print(user)
user.clear()  # This will remove all items from the dictionary
print(user)

print("=" * 50)

# update()

member = {"name": "Osama"}
print(member)
member["age"] = 36  # This will add a new key-value pair or update existing one
print(member)
member.update(
    {"country": "Egypt"}
)  # This will add a new key-value pair or update existing one
print(member)

print("=" * 50)

# copy()

main = {"name": "Osama"}

b = main.copy()  # This creates a shallow copy of the dictionary
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(
    main.keys()
)  # This returns a view object that displays a list of all the keys in the dictionary
print(
    main.values()
)  # This returns a view object that displays a list of all the values in the dictionary

# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {"name": "Osama"}
print(user)
print(
    user.setdefault("age", 36)
)  # This will return the value of 'age' if it exists, otherwise it will set 'age' to 36 and return 36
print(user)

print("=" * 40)

# popitem()

member = {"name": "Osama", "skill": "PS4"}
print(member)
member.update({"age": 36})  # This will add a new key-value pair
print(member.popitem())  # This will remove and return the last inserted key-value pair

print("=" * 40)

# items()

view = {"name": "Osama", "skill": "XBox"}

allItems = (
    view.items()
)  # This returns a view object that displays a list of all the key-value pairs in the dictionary
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "X"
print(
    dict.fromkeys(a, b)
)  # This creates a new dictionary with keys from 'a' and all values set to 'X'
