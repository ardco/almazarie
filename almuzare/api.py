# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
import frappe
import json
from PyPDF2 import PdfFileWriter
from frappe.utils.print_format import read_multi_pdf
from frappe.utils.print_format import download_pdf
from frappe.utils import getdate
from frappe import _, throw
from datetime import datetime
import json


@frappe.whitelist()

def barcode(doc, method):
    frappe.db.set_value('Sales Invoice' , doc.name , 'barcode' , doc.name)
    frappe.db.commit()

