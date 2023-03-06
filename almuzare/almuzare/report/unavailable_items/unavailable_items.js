// Copyright (c) 2016, Hadeel Milad and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Unavailable items"] = {
	"filters": [
		{
			fieldname:"last_stock_empty_date",
			label: __("last stock empty date"),
			fieldtype: "Date",
		},
	]
};
