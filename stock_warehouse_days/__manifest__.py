# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'WMS days management',
    'version': '1.1',
    'summary': 'Warehouse days',
    'description': """
Warehouse days Management
=======================
This module allows you to easily add warehouse days to the reordering rules for the calculation of stock supply.
    """,
    'website': 'https://www.rapidsoft.com.py',
    'author': 'Rapidsoft',
    'depends': ['stock_account', 'purchase','stock'],
    'category': 'Warehouse',
    'sequence': 16,
    'demo': [
    ],
    'data': [
        'data/orderpoint_data_cron.xml',
        'views/orderpoint_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}