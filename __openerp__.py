# -*- coding: utf-8 -*-
{
    'name': "VideoClub",

    'summary': """Manage movies and games""",

    'description': """
        VideoClub module for Movies and Games:
            - Partners
            - Rental
            - Article
            - Movies
            - Games
    """,

    'author': "Paolo Dávila",
    'website': "http://www.paolodavila.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/videoclub.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}