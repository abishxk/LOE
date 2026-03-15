import json

FILE = "data/users.json"


def load_users():

    try:

        with open(FILE, "r") as file:
            users = json.load(file)

        return users

    except:

        return []


def save_users(users):

    with open(FILE, "w") as file:

        json.dump(users, file, indent=4)


def signup():

    users = load_users()

    print("\n===== SIGNUP =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:

        if user["username"] == username:

            print("Username already exists")
            return

    new_user = {}

    new_user["username"] = username
    new_user["password"] = password

    users.append(new_user)

    save_users(users)

    print("Signup successful")


def login():

    users = load_users()

    print("\n===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    for user in users:

        if user["username"] == username and user["password"] == password:

            print("Login successful")
            return True

    print("Invalid credentials")
    return False