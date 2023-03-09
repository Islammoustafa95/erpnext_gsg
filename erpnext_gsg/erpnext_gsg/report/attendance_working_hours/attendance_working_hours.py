# Copyright (c) 2023, aseel-gh and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns, data = [], []
    data = get_data(filters)
    columns = get_columns()
    return columns, data


def get_data(filters):
    return frappe.db.get_all("Attendance", ['employee_name', 'attendance_date', 'check_in', 'check_out'],
                             filters=filters)


def get_columns():
    columns = [
        {'fieldname': 'employee', 'label': 'Employee', 'fieldtype': 'Link', 'options': 'Employee'},
        {'fieldname': 'employee_name', 'label': 'Employee Name', 'fieldtype': 'Data'},
        {'fieldname': 'attendance_date', 'label': 'Attendance Date', 'fieldtype': 'Date'},
        {'fieldname': 'check_in', 'label': 'Check in', 'fieldtype': 'Time'},
        {'fieldname': 'check_out', 'label': 'Check out', 'fieldtype': 'Time'},
    ]

    return columns
