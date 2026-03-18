from models import KPI, StaffingRequest, ActionRequired


class DashboardModule:

    def __init__(self, db_module):
        self.db_module = db_module

    def display_kpi(self):

        db = self.db_module.get_session()

        res = db.query(KPI).all()

        print("\n===== KPI =====\n")

        for r in res:
            print(r.kpiName, ":", r.kpiValue)

    def loe_graph(self):

        print("\nLOE GRAPH\n")

        print("DevOps        | ######")
        print("Cloud         | #####")
        print("Security      | ###")

    def show_action_required(self):

        db = self.db_module.get_session()

        res = db.query(ActionRequired).all()

        print("\n===== ACTION REQUIRED =====\n")

        if not res:
            print("No data")
            return
        for r in res:
            print(r.reqId, r.client, r.status)

    def show_sla_risk(self):

        print("\nSLA Risk Overview")
        print("1 All")
        print("2 LOE")
        print("3 Staffing")

        choice = input("Enter choice: ")

        # ================= SIMPLE IF ELSE =================

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

        else:
            print("Invalid choice")
            return

        # ================= PRINT =================

        print("\nSLA Risk Overview\n")

        for k in data:
            percent = data[k]

            bars = int(percent // 5)

            print(f"{k:<22} ({percent}%)  {'*' * bars}")

