import frappe
from erpnext.stock.doctype.material_request.material_request import make_stock_entry


def create_stock_entry(doc, method):
    if doc.material_request_type == "Material Transfer":
        stock_entry = make_stock_entry(doc.name)
        # stock_entry = frappe.new_doc("Stock Entry")
        stock_entry.stock_entry_type = doc.material_request_type
        stock_entry.from_warehouse = doc.set_from_warehouse

        for material_entry_item in doc.items:
            stock_entry.append("items", {"s_warehouse": material_entry_item.from_warehouse,
                                         "t_warehouse": material_entry_item.warehouse,
                                         "item_code": material_entry_item.item_code,
                                         "qty": material_entry_item.qty,
                                         # "material_request": doc.name
                                         })

            stock_entry.insert(ignore_permissions=True)
            stock_entry.submit()



#"material_request": "MAT-MR-2023-00003"