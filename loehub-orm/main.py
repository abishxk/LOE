from db_connection import engine
from models import Base, User, KPI, Graph, ActionRequired, StaffingRequest
import auth
import staffing
import dashboard

Base.metadata.create_all(bind=engine)

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("1 Dashboard")
        print("2 Staffing")
        print("3 Action Required")
        print("4 Logout")
        choice = input("Choice: ")

        if choice == "1":
            dashboard.show_dashboard()
        elif choice == "2":
            staffing.staffing_menu()
        elif choice == "3":
            dashboard.show_action_required()
        elif choice == "4":
            break

def start():
    while True:
        print("\nLOEHub System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")
        choice = input("Choice: ")

        if choice == "1":
            if auth.login():
                main_menu()
        elif choice == "2":
            auth.signup()
        elif choice == "3":
            break

start()