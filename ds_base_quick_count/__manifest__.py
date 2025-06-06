# -*- coding: utf-8 -*-
{
    'name': "Hitung Cepat",

    'summary': "Modul Dasar Untuk Hitung Cepat Pemilu",

    'description': "Hitung Cepat adalah perhitungan dilakukan secara cepat dengan menggunakan sistem informasi. Modul ini di gunakan untuk peritungan pemilu dengan cepat.",

    'author': "lOLI DESU",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/saksi.xml',
        'views/koordinator.xml',
        'views/calon.xml',
        'views/partai.xml',
        'views/tps.xml',
        'views/wilayah.xml',
        'views/pemilihan.xml',
        'views/paslon.xml',
        'views/hitung_cepat.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

