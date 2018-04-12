# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "print_limit"
app_title = "Print Limit"
app_publisher = "das"
app_description = "App to limit print. edit print.js in frappe-public-js-form"
app_icon = "octicon octicon-file-directory"
app_color = "#a99485"
app_email = "das@das.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/print_limit/css/print_limit.css"
# app_include_js = "/assets/print_limit/js/print_limit.js"

# include js, css files in header of web template
# web_include_css = "/assets/print_limit/css/print_limit.css"
# web_include_js = "/assets/print_limit/js/print_limit.js"

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

# Website user home page (by function)
# get_website_user_home_page = "print_limit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "print_limit.install.before_install"
# after_install = "print_limit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "print_limit.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"print_limit.tasks.all"
# 	],
# 	"daily": [
# 		"print_limit.tasks.daily"
# 	],
# 	"hourly": [
# 		"print_limit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"print_limit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"print_limit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "print_limit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "print_limit.event.get_events"
# }

