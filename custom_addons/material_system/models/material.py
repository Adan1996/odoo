from odoo import api, fields, models
from odoo.exceptions import ValidationError

class material (models.Model):
    _name = "material"
    _rec_name = "material_name"
    _description = "Material description"
	
    material_code = fields.Char(string="Code", required=True)
    material_name = fields.Char(string="Name", required=True)
    material_type = fields.Selection([('fabrics', 'Fabrics'), ('jeans', 'Jeans'), ('cottons', 'Cottons')], string="Type", required=True)
    material_buy_price = fields.Integer(string="Buy Price", store=True, required=True)
    supplier_id = fields.Many2one(string="Supplier", comodel_name='supplier', required=True)
    
    @api.constrains('material_buy_price')
    def check_material_buy_price(self):
        for record in self:
	        if record.material_buy_price < 100:
	            raise ValidationError("Buy Price must be greater than 100")