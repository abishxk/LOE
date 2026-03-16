from db_connection import SessionLocal
from models import StaffingRequest
from tabulate import tabulate
from models import ActionRequired

def show_dashboard():
    db = SessionLocal()
    requests = db.query(StaffingRequest).all()
    open_count = 0
    progress_count = 0
    closed_count = 0
    specialization_count = {}

    for r in requests:
        if r.status == "Open":
            open_count += 1
        elif r.status == "In Progress":
            progress_count += 1
        elif r.status == "Closed":
            closed_count += 1
        spec = r.specialization
        if spec in specialization_count:
            specialization_count[spec] += 1
        else:
            specialization_count[spec] = 1

    table = [
        ["Open", open_count],
        ["In Progress", progress_count],
        ["Closed", closed_count]
    ]

    print("\nDASHBOARD\n")
    print(tabulate(table, headers=["Status", "Count"], tablefmt="grid"))
    print("\nLOE In Progress by Specialization\n")

    for spec in specialization_count:
        count = specialization_count[spec]
        bar = ""
        for i in range(count):
            bar += "█"

        print(spec, "|", bar, "(", count, ")")

def show_action_required():
    db = SessionLocal()
    records = db.query(ActionRequired).all()

    table = []
    for r in records:
        row = [
            r.req_id,
            r.client,
            r.type,
            r.specialization,
            r.status,
            r.sla
        ]

        table.append(row)

    headers = [
        "Req ID",
        "Client",
        "Type",
        "Specialization",
        "Status",
        "SLA"
    ]

    print("\nACTION REQUIRED\n")

    if len(table) == 0:
        print("No pending actions")
    else:
        print(tabulate(table, headers=headers, tablefmt="grid"))