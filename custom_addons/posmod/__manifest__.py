{
    'name': 'POS Mod',
    'version': '14.0.1.0.0',
    'summary': 'This module can be modified POS',
    'description': """This module can be modified POS""",
    'category': 'Extra Tools',
    'author': '',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['point_of_sale'],
    'data': [
        'xml/view.xml',
        # 'security/ir.model.access.csv'
    ],
    # 'demo': [],
    # 'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'point_of_sale.assets': [
            "posmod/static/src/js/pos_config_button.js",
            "posmod/static/src/xml/pos_config_button.xml"
        ]
    }
}
