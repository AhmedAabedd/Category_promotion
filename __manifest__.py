# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Category Promotion',
    'version' : '1.0',
    'summary': 'Promotion per category',
    'sequence': 10,
    'description': '"Category Promotion software"',
    'category': 'Productivity',
    'website': 'https://www.proosoftcloud.com/',
    'depends' : ['mail',
                 'sale',
    ],
    'data': ['data/promotion_product.xml',
             'wizards/promotion_select_view.xml',
             'views/inherit_sale_order_view.xml',
             'views/inherit_product_view.xml',
             'views/menu.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
}