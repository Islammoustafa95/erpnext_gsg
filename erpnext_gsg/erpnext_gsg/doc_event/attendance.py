import frappe
from frappe.utils import time_diff_in_hours


def get_working_hours(doc, method):
    if not doc.check_in or not doc.check_out:
        doc.working_hours2 = 0

    if doc.check_in and doc.check_out:
        doc.working_hours2 = time_diff_in_hours(doc.check_out, doc.check_in)
