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


def show_dashboard():

    data = load_data()

    open_count = 0
    progress_count = 0
    closed_count = 0

    for record in data:

        if record["status"] == "Open":
            open_count = open_count + 1

        elif record["status"] == "In Progress":
            progress_count = progress_count + 1

        elif record["status"] == "Closed":
            closed_count = closed_count + 1

    print("\n========== DASHBOARD ==========\n")

    table = []

    table.append(["LOE In Progress", progress_count])
    table.append(["Pending Staff Assignment", open_count])
    table.append(["Completed Requests", closed_count])

    print(tabulate(table, headers=["Metric", "Count"], tablefmt="grid"))

    specialization_chart(data)


def specialization_chart(data):

    print("\nLOE by Specialization\n")

    specialization_count = {}

    for record in data:

        spec = record["specialization"]

        if spec in specialization_count:

            specialization_count[spec] = specialization_count[spec] + 1

        else:

            specialization_count[spec] = 1

    if len(specialization_count) == 0:

        print("No data available")
        return

    for spec in specialization_count:

        count = specialization_count[spec]

        bar = ""

        for i in range(count):

            bar = bar + "█"

        print(spec, "|", bar, "(", count, ")")