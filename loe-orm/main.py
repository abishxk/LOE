from database import DatabaseModule
from models import Base
from staffing import StaffingModule
from dashboard import DashboardModule


class MainModule:

    def __init__(self):
        self.db_module = DatabaseModule()

    def start_application(self):

        self.db_module.initialize_connection()

        Base.metadata.create_all(bind=self.db_module.connection)

        self.menu()

    def menu(self):

        staffing = StaffingModule(self.db_module)
        dashboard = DashboardModule(self.db_module)

        while True:

            print("\n========== MAIN MENU ==========")
            print("1 Dashboard")
            print("2 Staffing")
            print("3 Exit")

            choice = input("Enter: ")

            if choice == "1":
                dashboard.show_dashboard()

            elif choice == "2":
                self.staffing_menu(staffing)

            elif choice == "3":
                print("Exiting...")
                break

    def staffing_menu(self, staffing):

        while True:

            print("\n========== STAFFING ==========")
            print("1 View Requests")
            print("2 Add Request")
            print("3 Search")
            print("4 Back")

            choice = input("Enter: ")

            if choice == "1":
                staffing.display_staffing_table()

            elif choice == "2":
                staffing.add_staffing_record()

            elif choice == "3":
                staffing.search_staffing_data()

            elif choice == "4":
                break


if __name__ == "__main__":

    app = MainModule()
    app.start_application()