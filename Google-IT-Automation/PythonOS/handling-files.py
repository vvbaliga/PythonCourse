#!/usr/bin/env python3

import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    with open(csv_file_location) as employees:
        reader = csv.DictReader(employees)
        for row in reader:
            print(("{} has {} in {}").format(
                row["Full Name"], row["Username"], row["Department"]))


read_employees('/home/student-04-e64fee7cb66a/data/employees.csv')
