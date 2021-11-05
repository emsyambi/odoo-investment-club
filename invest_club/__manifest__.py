# -*- coding: utf-8 -*-
{
    'name' : 'Investment Club Management',
    'version' : '1.0',
    'summary': 'Investment Club Management software',
    'sequence': -100,
    'description': """Investment Club Management software""",
    'category': '',
    'website': 'https://www.bondsavingscheme.com',
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/slide_data_v12.xml',
        'data/slide_data_v13.xml',
        'data/slide_data_v14.xml',
        'views/member_view.xml',
        'views/sale_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
