# Author: Abdelrahman Mohamed
# Contact: < Abdo.Tasks@Gmail.Com , https://Github.com/abd0m0hamed >
# Project: Odoo 10 Customer Service. 
# Description: Odoo 10 Customer Service Module.
# License: Science not for Monopoly.

# -*- coding: utf-8 -*-
{
    'name': "cs",

    'summary': """
        Testing customer service module""",

    'description': """
        It's a customer service module created by Abdelrahman Mohamed to test creating Odoo Module
    """,

    'author': "Abdelrahman Mohamed",
    'website': "https://github.com/abd0m0hamed",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
}
