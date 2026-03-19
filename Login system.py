import json

users = []

# Load Date from File
def load_data():
    global users
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except:
        users = []

# Save Data
def save_data():
    with open("users.json", "w") as file:
        json.dump(users, file)

def register_user():

    username = input("Enter username: ")
    password = input("Enter your password: ")

    u = {"Username": username, "Password": password}
    
    for u in users:
        if u["Username"] == username:
            print("User exists already")
            return
    
    users.append(u)
    save_data()
    print("User registered successfully.")


def login_user():

    username = input("Enter username: ")
    password = input("Enter password: ")

    found = False

    for u in users:
        if u["Username"] == username and u["Password"] == password:
            print("Login successful!")
            found = True
            break
        else:
            print("Invalid credentials!")

load_data()
while True:
    print(".....Login System.....")
    print("1 Register user")
    print("2 Login user")
    print("3 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    elif choice == "3":
        print("Program ended!")
        break
    else:
        print("Invalid choice")
