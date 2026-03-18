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

            print("\n===== MAIN MENU =====")
            print("1 Dashboard")
            print("2 Staffing")
            print("3 Exit")

            choice = input("Enter: ")

            if choice == "1":

                dashboard.display_kpi()
                dashboard.loe_graph()
                dashboard.show_action_required()
                dashboard.show_sla_risk()

            elif choice == "2":

                while True:

                    print("\n===== STAFFING =====")
                    print("1 View Requests")
                    print("2 Add Request")
                    print("3 Back")

                    c = input("Enter: ")

                    if c == "1":
                        staffing.display_staffing_table()
                    elif c == "2":
                        staffing.add_staffing_record()
                    elif c == "3":
                        break

            elif choice == "3":
                break


if __name__ == "__main__":

    app = MainModule()
    app.start_application()
