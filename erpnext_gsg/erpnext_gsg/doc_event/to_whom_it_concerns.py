import frappe


def get_last_salary_slip(doc, method):
    salary_slip = frappe.db.get_list("Salary Slip", filters={"employee_name": doc.employee_name}, fields="base_gross_pay")
    doc.salary = str(salary_slip[0].base_gross_pay)
