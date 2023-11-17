# -*- coding: utf-8 -*-
{
    'name': "charcuteria",
    'summary': """tienda de charcuteria""",
    'description': """
        Modulo para gestionar una tienda de charcuteria
    """,
    'author': "Alejandro Esteban",
    'website': "http://www.salesianos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Ejecicio',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}