# 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
unique_list.pop()
print(unique_list)
print("-" * 25)


# 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
print("-" * 25)

# 3
nums = {1, 2, 3}
print(nums)
nums.clear()
print(nums)
nums.update({"A", "B"})
print(nums)
print("-" * 25)

# 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))
print("-" * 25)

# 5
Skills = {
    "One": {"name": "Html", "progress": "80%"},
    "Two": {"name": "Css", "progress": "90%"},
    "Three": {"name": "Js", "progress": "90%"},
}
print(f"{Skills["One"]["name"]} => {Skills["One"]["progress"]}")
print(f"{Skills["Two"]["name"]} => {Skills["Two"]["progress"]}")
print(f"{Skills["Three"]["name"]} => {Skills["Three"]["progress"]}")

Skills["Four"] = {"name": "Python", "progress": "100%"}
print(f"{Skills["Four"]["name"]} => {Skills["Four"]["progress"]}")

