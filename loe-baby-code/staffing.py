from models import StaffingRequest, ActionRequired
from tabulate import tabulate


class StaffingModule:

    def __init__(self, db_module):
        self.db_module = db_module

    def print_table(self, data):

        table = []

        for r in data:
            table.append([
                r.reqId,
                r.client,
                r.project,
                r.specialization,
                r.status,
                r.projectStartDate
            ])

        if table:
            print(tabulate(
                table,
                headers=["REQ ID", "CLIENT", "PROJECT", "SPEC", "STATUS", "START DATE"],
                tablefmt="grid"
            ))
        else:
            print("No records found")

    def display_staffing_table(self):

        db = self.db_module.get_session()

        status_filter = None
        spec_filter = None
        search_term = None

        statuses = ["Open", "In Progress", "Closed"]
        specs = ["Backend", "Frontend", "DevOps", "Data Science", "AI/ML", "Cloud", "Security"]

        while True:

            all_data = db.query(StaffingRequest).all()

            filtered_data = []

            for r in all_data:

                match = True

                if status_filter and r.status != status_filter:
                    match = False

                if spec_filter and r.specialization != spec_filter:
                    match = False

                if search_term:
                    text = search_term.lower()
                    if text not in r.client.lower() and text not in r.project.lower() and text not in r.reqId.lower():
                        match = False

                if match:
                    filtered_data.append(r)

            print("\n===== STAFFING REQUESTS =====")
            print(f"\nFilters → Status: {status_filter or 'All'} | Spec: {spec_filter or 'All'} | Search: {search_term or 'None'}\n")

            self.print_table(filtered_data)

            print("\nOptions:")
            print("1 Status Filter")
            print("2 Specialization Filter")
            print("3 Search")
            print("4 Clear Filters")
            print("5 Back")

            choice = input("Enter: ")

            if choice == "1":

                print("\nSelect Status:")
                print("0 All")
                for i in range(len(statuses)):
                    print(f"{i+1}. {statuses[i]}")

                s = input("Enter: ")

                if s == "0":
                    status_filter = None
                elif s.isdigit() and 1 <= int(s) <= len(statuses):
                    status_filter = statuses[int(s) - 1]

            elif choice == "2":

                print("\nSelect Spec:")
                print("0 All")
                for i in range(len(specs)):
                    print(f"{i+1}. {specs[i]}")

                s = input("Enter: ")

                if s == "0":
                    spec_filter = None
                elif s.isdigit() and 1 <= int(s) <= len(specs):
                    spec_filter = specs[int(s) - 1]

            elif choice == "3":

                search_term = input("Search: ")

            elif choice == "4":

                status_filter = None
                spec_filter = None
                search_term = None

            elif choice == "5":
                break

    def add_staffing_record(self):

        db = self.db_module.get_session()

        obj = StaffingRequest()

        obj.reqId = input("Req ID: ")
        obj.client = input("Client: ")
        obj.project = input("Project: ")

        specs = ["Backend", "Frontend", "DevOps", "Data Science", "AI/ML", "Cloud", "Security"]

        print("\nSelect Specialization:")
        for i in range(len(specs)):
            print(f"{i + 1}. {specs[i]}")

        s = input("Enter: ")

        if s.isdigit() and 1 <= int(s) <= len(specs):
            obj.specialization = specs[int(s) - 1]
        else:
            print("Invalid choice, defaulting to Backend")
            obj.specialization = "Backend"

        statuses = ["Open", "In Progress", "Closed"]

        print("\nSelect Status:")
        for i in range(len(statuses)):
            print(f"{i + 1}. {statuses[i]}")

        s = input("Enter: ")

        if s.isdigit() and 1 <= int(s) <= len(statuses):
            obj.status = statuses[int(s) - 1]
        else:
            print("Invalid choice, defaulting to Open")
            obj.status = "Open"

        obj.projectStartDate = input("Start Date (YYYY-MM-DD): ")

        db.add(obj)
        db.commit()

        print("Record Added")

        if obj.status != "Closed":
            action = ActionRequired()

            action.reqId = obj.reqId
            action.client = obj.client
            action.type = "Staff"
            action.specialization = obj.specialization
            action.status = obj.status
            action.sla = "Pending"

            db.add(action)
            db.commit()
