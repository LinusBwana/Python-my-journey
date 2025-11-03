user_name = input("Enter the user name: ")

if len(user_name) > 12:
    print("User name can not be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("User name can not have spaces")
elif not user_name.isalpha():
    print("User name can not have digits")
else:
    print(f"Welcome {user_name}")
