from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

correct_username = "123456789"
correct_password = "demo123"

if username == correct_username and password == correct_password:
    print("\nWelcome Ambika!")
    print("You are successfully logged in!")

elif username != correct_username and password == correct_password:
    print("\nIncorrect username.")

elif username == correct_username and password != correct_password:
    print("\nIncorrect password.")

else:
    print("\nIncorrect username and password.")