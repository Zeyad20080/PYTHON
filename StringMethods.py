# String Methods

sep = (
    " --------------------------------------- --------------------------------------- "
)

a = "         I love python!         "
print(a.strip())  # Removes leading and trailing whitespace
print(a.lstrip())  # Removes leading whitespace
print(a.rstrip())  # Removes trailing whitespace
print(sep)

b = "I love python!"
print(b.lower())  # Converts to lowercase
print(b.upper())  # Converts to uppercase
print(b.title())  # Converts to title case
print(b.capitalize())  # Capitalizes the first character
print(b.swapcase())  # Swaps case of all characters
print(sep)

c, d, e, f = "1", "11", "111", "1111"
print(c.zfill(3))  # Pads with zeros to fill width of 3
print(d.zfill(3))  # Pads with zeros to fill width of 3
print(e.zfill(3))  # Pads with zeros to fill width of 3
print(f.zfill(3))  # Pads with zeros to fill width of 3
print(sep)

a = "I love python!"
print(a.split())  # Splits the string into a list of words
a = "I-love-python!"
print(a.split("-"))  # Splits the string by the hyphen

mylsit = ["Hello", "World", "Python"]
print(" ".join(mylsit))  # Joins the list into a string with spaces
print("-".join(mylsit))  # Joins the list into a string with hyphens
print(sep)

e = "Zeyad"
print(e.center(10, "#"))  # Centers the string in a field of width 10
print(e.rjust(10, "#"))  # Right-justifies the string in a field of width 10
print(e.ljust(10, "#"))  # Left-justifies the string in a field of width 10
print(sep)

f = "I love python!"
print(f.find("love"))  # Finds the index of the substring 'love'
print(
    f.index("love")
)  # Finds the index of the substring 'love', raises error if not found
print(f.count("o"))  # Counts occurrences of 'o'
print(f.count("o", 0, 6))  # Counts occurrences of 'o'
print(f.replace("love", "hate"))  # Replaces 'love' with 'hate'
print(f.replace("love", "hate", 1))  # Replaces first occurrence of 'love' with 'hate'
print(sep)


f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())  # Splits the string into lines
print(f.splitlines(keepends=True))  # Keeps the newline characters

print(sep)

g = "Hello\tWorld"
print(g.expandtabs())  # Expands tabs to spaces, default is 8
print(g.expandtabs(2))  # Expands tabs to 2 spaces
print(g.expandtabs(10))  # Expands tabs to 10 spaces
print(sep)


e = "I love python!"
print(e.startswith("I love"))  # Checks if the string starts with 'I love'
print(e.endswith("python!"))  # Checks if the string ends with 'python!'
print(e.startswith("I love", 0, 10))  # Checks if the substring 'I love' is at the start
print(e.endswith("python!", 0, 10))  # Checks if the substring 'python!' is at the end
print(e.istitle())  # Checks if the string is in title case
print(e.isupper())  # Checks if the string is in uppercase
print(e.islower())  # Checks if the string is in lowercase
print(e.isalpha())  # Checks if the string contains only alphabetic characters
print(e.isalnum())  # Checks if the string contains only alphanumeric characters
print(e.isdigit())  # Checks if the string contains only digits
print(e.isnumeric())  # Checks if the string contains only numeric characters
print(e.isascii())  # Checks if the string contains only ASCII characters
print(e.isprintable())  # Checks if the string is printable
print(e.isidentifier())  # Checks if the string is a valid identifier
print(e.isdecimal())  # Checks if the string contains only decimal characters
print(e.isspace())  # Checks if the string contains only whitespace characters
print(e.removeprefix("I love "))  # Removes the prefix 'I love '
print(e.removesuffix("python!"))  # Removes the suffix 'python!'
print(e.removeprefix("I"))  # Removes the prefix 'I'
print(e.removesuffix("!"))  # Removes the suffix '!'
print(e.removeprefix("I love python!"))  # Removes the entire string if it matches
print(e.removesuffix("I love python!"))  # Removes the entire string if it matches
print(e.removeprefix("I love python! "))  # No change
print(e.removesuffix(" I love python!"))  # No change
print(sep)
