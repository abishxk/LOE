from db_connection import SessionLocal
from models import StaffingRequest
from tabulate import tabulate
from models import ActionRequired


def add_request():
    db = SessionLocal()
    req = StaffingRequest()
    print("\nADD STAFFING REQUEST")
    req.spec_filter = input("Spec Filter: ")
    req.req_id = input("Req ID: ")
    req.client = input("Client: ")
    req.project = input("Project: ")
    req.specialization = input("Specialization: ")
    req.resource = input("Resource: ")
    req.status = input("Status (Open/In Progress/Closed): ")
    req.project_start_date = input("Project Start Date: ")
    db.add(req)
    db.commit()

    if req.status == "Open":
        action = ActionRequired()
        action.req_id = req.req_id
        action.client = req.client
        action.type = "Staff"
        action.specialization = req.specialization
        action.status = req.status
        action.sla = "Pending"
        db.add(action)
        db.commit()
    print("Request added successfully")

def view_requests():
    db = SessionLocal()
    records = db.query(StaffingRequest).all()
    table = []
    for r in records:
        row = [
            r.staff_id,
            r.req_id,
            r.client,
            r.project,
            r.specialization,
            r.resource,
            r.status,
            r.project_start_date
        ]
        table.append(row)

    headers = [
        "ID",
        "Req ID",
        "Client",
        "Project",
        "Specialization",
        "Resource",
        "Status",
        "Start Date"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))


def staffing_menu():
    while True:
        print("\nSTAFFING MENU")
        print("1 View Requests")
        print("2 Add Request")
        print("3 Back")

        choice = input("Choice: ")

        if choice == "1":
            view_requests()
        elif choice == "2":
            add_request()
        elif choice == "3":
            break