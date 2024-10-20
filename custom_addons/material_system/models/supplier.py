from odoo import fields, models

class supplier(models.Model):
    _name = 'supplier'
    _rec_name = 'supplier_name'
    _description = 'Supplier descriptions'
    
    supplier_name = fields.Char(string='Supplier')