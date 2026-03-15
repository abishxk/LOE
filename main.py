import auth
import dashboard
import staffing


def start():

    while True:

        print("\n==========================")
        print("       LOEHub System")
        print("==========================")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            login_success = auth.login()

            if login_success == True:
                main_menu()

        elif choice == "2":

            auth.signup()

        elif choice == "3":

            print("Exiting system")
            break

        else:

            print("Invalid option")


def main_menu():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Dashboard")
        print("2. Staffing")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            dashboard.show_dashboard()

        elif choice == "2":

            staffing.staffing_menu()

        elif choice == "3":

            print("Logged out")
            break

        else:

            print("Invalid option")


if __name__ == "__main__":
    start()