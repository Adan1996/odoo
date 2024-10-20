from odoo.test.common import TransactionCase

class TestMaterial(TransactionCase):
    
    def setUp(self, *args, **kwargs):
        super(TestMaterial, self).setUp()
        self.material_01_record = self.env['material'].create({
            'code': 'M010',
            'name': 'Material 1',
            'type': 'fabrics',
            'buy_price': 100.0,
            'supplier': 'CV Berkah Jaya'
        })
        
    def test_01_material_values(self):
        material_id = self.material_01_record
        
        self.assertRecordValues(material_id, [{
            'code': 'M010',
            'name': 'Material 1',
            'type': 'fabrics',
            'buy_price': 100.0,
            'supplier': 'CV Berkah Jaya'
        }])