# -*- coding: utf-8 -*-
{
    'name' : 'Direct Investment Tracking',
    'version' : '14.0.1',
    'summary': "Direct Investment Tracking",
    'sequence': 14,
    'description': """
                    """,
    'category': 'Investments',
    'author': 'Deekshith HM',
    'maintainer': 'Wayonc Technologies',
    'website': '',
    'depends': ['base','mail','contacts'],
    'data': [
    		'security/ir.model.access.csv',
            'data/ir_sequence_data.xml',
            'views/res_client_views.xml',
            'views/res_partner_views.xml',
             'views/processing_charges_rule_views.xml',
             
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
