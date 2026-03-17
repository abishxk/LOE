from models import StaffingRequest
from tabulate import tabulate


class DashboardModule:

    def __init__(self, db_module):
        self.db_module = db_module

    def show_dashboard(self):

        db = self.db_module.get_session()
        data = db.query(StaffingRequest).all()

        print("\n========== DASHBOARD ==========\n")

        # ================= KPIs =================

        loe_static = 6  # STATIC
        pending_staff = len([r for r in data if r.status == "Open"])
        nearing_sla = 2  # STATIC

        kpi = [
            ["LOE In Progress", loe_static],
            ["Pending Staff Assignment", pending_staff],
            ["Nearing SLA Breach", nearing_sla]
        ]

        print(tabulate(kpi, headers=["Metric", "Value"], tablefmt="grid"))

        # ================= LOE GRAPH (STATIC) =================

        print("\nLOE In Progress by Specialization\n")

        static_graph = {
            "Data Engineering": 12,
            "Cloud Architecture": 8,
            "DevOps": 6,
            "Security": 5,
            "Data Science": 3
        }

        for k in static_graph:
            print(f"{k:<20} | {'█' * static_graph[k]} ({static_graph[k]})")

        # ================= ACTION REQUIRED =================

        print("\nACTION REQUIRED\n")

        table = []

        for r in data:
            if r.status != "Closed":
                table.append([
                    r.reqId,
                    r.client,
                    "Staff",
                    r.specialization,
                    r.status,
                    "1d remaining"
                ])

        print(tabulate(
            table,
            headers=["REQ ID", "CLIENT", "TYPE", "SPEC", "STATUS", "SLA"],
            tablefmt="grid"
        ))

        # ================= SLA (STATIC UI STYLE) =================

        self.show_sla_risk()

    def show_sla_risk(self):

        while True:

            print("\nSLA Risk Filter")
            print("1 All")
            print("2 LOE")
            print("3 Staffing")
            print("4 Back")

            choice = input("Select filter: ")

            # ================= STATIC DATA =================

            if choice == "1":
                data = {
                    "On Time": 70,
                    "<4 Hours Remaining": 20,
                    "Breached": 10
                }

            elif choice == "2":
                data = {
                    "On Time": 60,
                    "<4 Hours Remaining": 30,
                    "Breached": 10
                }

            elif choice == "3":
                data = {
                    "On Time": 80,
                    "<4 Hours Remaining": 10,
                    "Breached": 10
                }

            elif choice == "4":
                break

            else:
                print("Invalid choice")
                continue

            # ================= DISPLAY =================

            print("\nSLA Risk Overview\n")

            for k, v in data.items():

                bars = int(v // 5)  # scale (5% = 1 dot)

                print(f"{k:<22} ({v}%)  {'●' * bars}")