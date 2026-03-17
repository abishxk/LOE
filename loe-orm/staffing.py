from models import StaffingRequest
from tabulate import tabulate


class StaffingModule:

    def __init__(self, db_module):
        self.db_module = db_module

    def display_staffing_table(self):

        db = self.db_module.get_session()

        while True:

            # ================= SHOW ALL DATA FIRST =================
            data = db.query(StaffingRequest).all()

            print("\n===== STAFFING REQUESTS =====\n")

            self.print_table(data)

            # ================= OPTIONS =================
            print("\nOptions:")
            print("1 Filter by Status")
            print("2 Filter by Specialization")
            print("3 Search")
            print("4 Back")

            choice = input("Enter choice: ")

            # ================= STATUS FILTER =================
            if choice == "1":

                while True:

                    statuses = ["Open", "In Progress", "Closed"]

                    print("\nFilter by Status:")
                    for i in range(len(statuses)):
                        print(f"{i + 1}. {statuses[i]}")
                    print(print("4 Back"))
                    s = input("Enter: ")

                    if s == "4":
                        break

                    elif s.isdigit() and 1 <= int(s) <= len(statuses):

                        selected = statuses[int(s) - 1]

                        filtered = db.query(StaffingRequest).filter(
                            StaffingRequest.status == selected
                        ).all()

                        print(f"\nFiltered by Status: {selected}\n")
                        self.print_table(filtered)

                    else:
                        print("Invalid choice")

            # ================= SPECIALIZATION FILTER =================
            elif choice == "2":

                while True:

                    specs = ["Backend", "Frontend", "DevOps", "Data Science", "AI/ML", "Cloud", "Security"]

                    print("\nFilter by Specialization:")

                    for i in range(len(specs)):
                        print(f"{i + 1}. {specs[i]}")
                    print("8 Back")
                    s = input("Enter: ")

                    if s == "8":
                        break

                    elif s.isdigit() and 1 <= int(s) <= len(specs):

                        selected = specs[int(s) - 1]

                        filtered = db.query(StaffingRequest).filter(
                            StaffingRequest.specialization == selected
                        ).all()

                        print(f"\nFiltered by Spec: {selected}\n")
                        self.print_table(filtered)

                    else:
                        print("Invalid choice")

            # ================= SEARCH =================
            elif choice == "3":

                term = input("\nSearch (client / project / req id): ")

                results = db.query(StaffingRequest).filter(
                    (StaffingRequest.client.ilike(f"%{term}%")) |
                    (StaffingRequest.project.ilike(f"%{term}%")) |
                    (StaffingRequest.reqId.ilike(f"%{term}%"))
                ).all()

                print("\nSearch Results:\n")
                self.print_table(results)

            # ================= BACK =================
            elif choice == "4":
                break

            else:
                print("Invalid choice")

    def add_staffing_record(self):

        db = self.db_module.get_session()

        obj = StaffingRequest()

        print("\n===== ADD STAFFING REQUEST =====")

        obj.reqId = input("Req ID (ex: STAFF-001): ")
        obj.client = input("Client: ")
        obj.project = input("Project: ")

        # Specialization
        specs = ["Backend", "Frontend", "DevOps", "Data Science", "AI/ML", "Cloud", "Security"]

        print("\nSelect Specialization:")
        for i in range(len(specs)):
            print(f"{i+1}. {specs[i]}")

        obj.specialization = specs[int(input("Enter: ")) - 1]

        # Status
        statuses = ["Open", "In Progress", "Closed"]

        print("\nSelect Status:")
        for i in range(len(statuses)):
            print(f"{i+1}. {statuses[i]}")

        obj.status = statuses[int(input("Enter: ")) - 1]

        obj.projectStartDate = input("Start Date (YYYY-MM-DD): ")

        db.add(obj)
        db.commit()

        print("✅ Record Added")

    def search_staffing_data(self):

        db = self.db_module.get_session()

        term = input("Search: ")

        results = db.query(StaffingRequest).filter(
            StaffingRequest.client.ilike(f"%{term}%")
        ).all()

        table = []

        for r in results:
            table.append([
                r.reqId,
                r.client,
                r.project,
                r.specialization,
                r.status
            ])

        print(tabulate(
            table,
            headers=["REQ ID", "CLIENT", "PROJECT", "SPEC", "STATUS"],
            tablefmt="grid"
        ))

    def print_table(self, data):

        from tabulate import tabulate

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