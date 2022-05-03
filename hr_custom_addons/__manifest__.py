# -*- coding: utf-8 -*-
{
    'name' : 'Custom addons for HR',
    'version' : '14.0.1',
    'summary': "Addon feature for HR module",
    'sequence': 14,
    'description': """
                    """,
    'category': 'HR',
    'author': 'Deekshith HM',
    'maintainer': 'Wayonc Technologies',
    'website': '',
    'depends': ['hr','base'],
    'data': [
    		'data/ir_sequence.xml',
             'views/hr_employee_views.xml',
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
