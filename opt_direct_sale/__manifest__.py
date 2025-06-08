{
    'name': 'Direct Sales',
    'version': '17.0.1.0',
    'summary': 'Direct sale management for Optura Technologies',
    'description': '''Module to manage the automated invoice creation, Delivery and its directly downloaded 
    when confirming a sale order in odoo. So small businesses can manage their sales without 
    handling invoice after sales
    ''',
    'author': 'Optura Technologies',
    'website': 'https://opturatech.com',
    'category': 'Sales',
    'depends': ['sale_management','account','stock'],
    'data': [
        # Add your data files here, e.g. 'views/sale_order_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}