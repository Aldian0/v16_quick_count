# -*- coding: utf-8 -*-
{
    'name': "WEB Quick Count",

    'summary': "Modul Tambahan Untuk Web Publik Hitung Cepat Pemilu",

    'description': "Modul Tmabaha Untuk Web Publik Hitung Cepat Pemilu",

    'author': "lOLI DESU",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.1',

    # any module necessary for this one to work correctly
    'depends': ['base','ds_base_quick_count','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/header_menu.xml',
        'views/inherit_res_company.xml',

        # 'views/landing_page.xml',
        # 'views/pengisian.xml',

        'views/website/home.xml',
        'views/website/pengisian_paslon.xml',
        'views/website/pengisian.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css'
            # 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js',
            # 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css',
            # 'http://code.jquery.com/jquery-1.11.1.min.js',

            # '/ds_web_quick_count/static/src/js/script.js'
        ],
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

