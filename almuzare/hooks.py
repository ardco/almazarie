# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "almuzare"
app_title = "Almuzare"
app_publisher = "Hadeel Milad"
app_description = "edit the method of calculating the Landed Cost Voucher by adding the CBM method"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hadeel.milad@ard.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/almuzare/css/almuzare.css"
# app_include_js = "/assets/almuzare/js/almuzare.js"

# include js, css files in header of web template
# web_include_css = "/assets/almuzare/css/almuzare.css"
# web_include_js = "/assets/almuzare/js/almuzare.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "almuzare/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "almuzare.install.before_install"
# after_install = "almuzare.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "almuzare.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
    "custom" : "almuzare.frappe_custom.override.make_options_editable"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Sales Invoice":{
        "on_submit":"almuzare.api.barcode"
    }

}

	

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"almuzare.tasks.all"
# 	],
# 	"daily": [
# 		"almuzare.tasks.daily"
# 	],
# 	"hourly": [
# 		"almuzare.tasks.hourly"
# 	],
# 	"weekly": [
# 		"almuzare.tasks.weekly"
# 	]
# 	"monthly": [
# 		"almuzare.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "almuzare.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "almuzare.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "almuzare.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]



fixtures = [
    "Custom Field"
]
