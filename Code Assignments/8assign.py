# 1
name = input("Enter Your Name: ").strip().capitalize()

print(f"Hello {name}, Happy to see you here")

print("*" * 50)

# 2
age = int(input("Enter Your Age: ").strip())

if age < 16:
    print("You are too young")
else:
    print("You are old enough")

print("*" * 50)

# 3
firstName = input("Enter Your First Name: ").strip().capitalize()
lastName = input("Enter Your Last Name: ").strip().capitalize()

print(f"Hello {firstName} {lastName:.1s}., Happy to see you here")

print("*" * 50)

# 4
email = input("Enter Your Email: ").strip().lower()

atPosition = email.index("@")
dotPosition = email.rindex(".")

print(f"Your name is {email[:atPosition]}")
print(f"Your Email Service provider is {email[atPosition+1:dotPosition]}")
print(f"Your Domain is {email[dotPosition+1:]}")
