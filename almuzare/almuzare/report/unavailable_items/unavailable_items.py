# Copyright (c) 2013, Hadeel Milad and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe import _

# def execute(filters=None):
#     columns = [
#         {"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
#         {"label": _("Item Name"), "fieldname": "item_name", "fieldtype": "Data"},
#         {"label": _("Last Stock Empty Date"), "fieldname": "last_stock_empty_date", "fieldtype": "Datetime"},
#         {"label": _("Duration since Stock Empty (Days)"), "fieldname": "duration_since_stock_empty", "fieldtype": "Int"},
#     ]

#     data = frappe.db.sql("""
#         SELECT `tabItem`.item_code, `tabItem`.item_name, MAX(`tabBin`.modified) AS last_stock_empty_date,
#             DATEDIFF(NOW(), MAX(`tabBin`.modified)) AS duration_since_stock_empty
#         FROM `tabItem`
#         LEFT JOIN `tabBin` ON `tabItem`.item_code = `tabBin`.item_code
#         WHERE `tabBin`.actual_qty <= 0
#         GROUP BY `tabItem`.name
#         HAVING duration_since_stock_empty >= {0}
#         ORDER BY duration_since_stock_empty DESC
#     """.format(filters.get("duration_in_days")), as_dict=True)

#     return columns, data
def execute(filters=None):
	today = frappe.utils.nowdate()
	if not filters:
		filters = {"last_stock_empty_date": today, "duration_in_days": 30}

	return get_columns(), get_data(filters)

def get_columns():
	columns = [
        {"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
        {"label": _("Item Name"), "fieldname": "item_name", "fieldtype": "Data"},
        {"label": _("Last Stock Empty Date"), "fieldname": "last_stock_empty_date", "fieldtype": "Datetime"},
        {"label": _("Duration since Stock Empty (Days)"), "fieldname": "duration_since_stock_empty", "fieldtype": "Int"},
    ]
	return(columns)

def get_data(filters):
	# data = frappe.db.sql("""
    #     SELECT `tabItem`.item_code, `tabItem`.item_name, `tabItem`.end_of_life , MAX(`tabBin`.modified) AS last_stock_empty_date,
    #         DATEDIFF(NOW(), MAX(`tabBin`.modified)) AS duration_since_stock_empty
    #     FROM `tabItem`
    #     LEFT JOIN `tabBin` ON `tabItem`.item_code = `tabBin`.item_code
    #     WHERE `tabBin`.actual_qty <= 0
    #     GROUP BY `tabItem`.name HAVING duration_since_stock_empty >= 2  """, as_dict=True)
	# print(f"\n\n\n{filters}\n\n\n")
	data = frappe.db.sql("""
        SELECT `tabItem`.item_code, `tabItem`.item_name, MAX(`tabBin`.modified) AS last_stock_empty_date,
            DATEDIFF(NOW(), MAX(`tabBin`.modified)) AS duration_since_stock_empty        FROM `tabItem`
        LEFT JOIN `tabBin` ON `tabItem`.item_code = `tabBin`.item_code
        WHERE `tabBin`.actual_qty <= 0
        AND `tabBin`.modified <= %(last_stock_empty_date)s
        GROUP BY `tabItem`.name
        HAVING duration_since_stock_empty >= 0
        ORDER BY duration_since_stock_empty DESC
    """, {
        "last_stock_empty_date": filters.get("last_stock_empty_date") }, as_dict=True)


	return data