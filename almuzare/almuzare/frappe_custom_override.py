from frappe.custom.doctype.customize_form.customize_form import CustomizeForm
from frappe.utils import cint
from frappe.model.document import Document
class make_options_editable(Document):
   def allow_property_change(self, prop, meta_df, df):
    ALLOWED_OPTIONS_CHANGE = ('Read Only', 'HTML', 'Select','Data')