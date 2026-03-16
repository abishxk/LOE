from db_connection import SessionLocal
from models import User


def signup():
    db = SessionLocal()
    print("\nSIGNUP")
    username = input("Username: ")
    password = input("Password: ")
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        print("Username already exists")
        return
    user = User()
    user.username = username
    user.password = password
    db.add(user)
    db.commit()
    print("Signup successful")

def login():
    db = SessionLocal()
    print("\nLOGIN")
    username = input("Username: ")
    password = input("Password: ")
    user = db.query(User).filter(User.username == username).first()
    if user and user.password == password:
        print("Login successful")
        return True
    print("Invalid credentials")
    return False