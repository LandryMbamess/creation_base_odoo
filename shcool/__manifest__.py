# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """
        test d'aptitude""",

    'description': """
        test pour l'aplication et assoire les bases
    """,

    'author': "My Company",
    'website': "http://github.com/LandryMbamess",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/departement.xml',
        'views/student.xml',
        'views/professor.xml',
        'views/classroom.xml',
        'views/course.xml',
        'data/template_mail.xml',
        'data/template_mail_student.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

