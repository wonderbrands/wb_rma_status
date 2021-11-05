# -*- coding: utf-8 -*-
{
    'name': "RMA Status",

    'summary': """
        Se agregan campos al formulario orden de venta para conocer si esta cuenta con una orden de devolución""",

    'description': """
        Estatus de producto para conocer si es un producto devuelto
    """,

    'author': "Wonder Brands",
    'website': "https://wonderbrands.co/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale',
        'rma_ept',
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': False,
    'installable': True,
}