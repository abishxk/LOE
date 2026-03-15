import json
from tabulate import tabulate

FILE = "data/staffing.json"


def load_data():

    try:

        with open(FILE, "r") as file:

            data = json.load(file)

        return data

    except:

        return []


def save_data(data):

    with open(FILE, "w") as file:

        json.dump(data, file, indent=4)


def staffing_menu():

    while True:

        print("\n========== STAFFING ==========")
        print("1. View Requests")
        print("2. Add Request")
        print("3. Search Request")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            view_requests()

        elif choice == "2":

            add_request()

        elif choice == "3":

            search_request()

        elif choice == "4":

            break

        else:

            print("Invalid option")


def view_requests():

    data = load_data()

    if len(data) == 0:

        print("No requests available")
        return

    table = []

    for record in data:

        row = []

        row.append(record["req_id"])
        row.append(record["client"])
        row.append(record["project"])
        row.append(record["specialization"])
        row.append(record["assigned_to"])
        row.append(record["status"])
        row.append(record["start_date"])

        table.append(row)

    headers = [
        "Req ID",
        "Client",
        "Project",
        "Specialization",
        "Assigned To",
        "Status",
        "Start Date"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))


def add_request():

    data = load_data()

    print("\n===== ADD REQUEST =====")

    new_request = {}

    new_request["req_id"] = input("Req ID: ")
    new_request["client"] = input("Client: ")
    new_request["project"] = input("Project: ")
    new_request["specialization"] = input("Specialization: ")
    new_request["assigned_to"] = input("Assigned To: ")
    new_request["status"] = input("Status (Open/In Progress/Closed): ")
    new_request["start_date"] = input("Start Date: ")

    data.append(new_request)

    save_data(data)

    print("Request added successfully")


def search_request():

    data = load_data()

    keyword = input("Search client or project: ")

    keyword = keyword.lower()

    results = []

    for record in data:

        client = record["client"].lower()
        project = record["project"].lower()

        if keyword in client or keyword in project:

            row = []

            row.append(record["req_id"])
            row.append(record["client"])
            row.append(record["project"])
            row.append(record["specialization"])
            row.append(record["assigned_to"])
            row.append(record["status"])
            row.append(record["start_date"])

            results.append(row)

    if len(results) > 0:

        headers = [
            "Req ID",
            "Client",
            "Project",
            "Specialization",
            "Assigned To",
            "Status",
            "Start Date"
        ]

        print(tabulate(results, headers=headers, tablefmt="grid"))

    else:

        print("No matching records found")