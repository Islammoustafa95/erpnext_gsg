import datetime
from datetime import datetime

import frappe
from frappe.utils import time_diff_in_hours


def get_hours(doc, method):
    from_time = datetime.strptime(doc.from_time, "%H:%M:%S")
    to_time = datetime.strptime(doc.to_time, "%H:%M:%S")

    if from_time >= to_time:
        frappe.throw("From Time must be before To Time")

    if not doc.from_time or not doc.to_time:
        doc.hours = 0

    if doc.from_time and doc.to_time:
        doc.hours = time_diff_in_hours(doc.to_time, doc.from_time)

    department = doc.department
    excuse_hours_allowed = frappe.db.get_value("Department", department, "excuse_hours_alowed")
    if doc.hours > float(excuse_hours_allowed):
        frappe.throw("Excuse hours allowed for your department are " + excuse_hours_allowed)

    # //////////////////////////////////////////////////////////////////////////////////////////

    excuse_date = datetime.strptime(str(doc.excuse_date), "%Y-%m-%d")
    date1 = datetime.date(excuse_date)
    current_month = str(date1.month)
    current_year = str(date1.year)

    month_start = current_year + "-" + current_month + "-1"
    stat_of_the_month = datetime.strptime(str(month_start), "%Y-%m-%d")

    month_end = current_year + "-" + current_month + "-31"
    end_of_the_month = datetime.strptime(str(month_end), "%Y-%m-%d")

    list = frappe.db.get_list("Employee Excuse application",
                              filters={"employee": doc.employee, "excuse_date": ["between", (stat_of_the_month, end_of_the_month)]}, fields="hours")

    mylist = []
    for i in list:
        for value in i.values():
            mylist.append(value)

    current_month_hours = 0.0
    for item in mylist:
        current_month_hours = current_month_hours + float(item)

    # doc.reason = str(mylist)

    # //////////////////////////////////////////////////////////////////////////////////////////

    if current_month_hours > float(excuse_hours_allowed):
        frappe.throw(" You already used all excuse hours allowed for this month! ")



