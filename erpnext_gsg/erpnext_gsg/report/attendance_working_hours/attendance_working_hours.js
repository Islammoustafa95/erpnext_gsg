// Copyright (c) 2023, aseel-gh and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
	{ fieldname: 'employee', label: __('Employee'), fieldtype: 'Link', options: 'Employee'},
	{ fieldname: 'department', label: __('Department'), fieldtype: 'Link', options: 'Department'},
	{ fieldname: 'from_date', label: __('From Date'), fieldtype: 'Date'},
	{ fieldname: 'to_date', label: __('To Date'), fieldtype: 'Date'}

	]
};

//“From Date”, “To Date”, “Employee” and “Department”