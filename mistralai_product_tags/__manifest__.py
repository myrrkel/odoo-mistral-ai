# Copyright (C) 2023 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/algpl.html).
{
    'name': 'Mistral AI Product Tags',
    'version': '16.0.0.0',
    'author': 'Michel Perrocheau',
    'website': 'https://github.com/myrrkel',
    'summary': "Generate product tags with Mistral AI",
    'sequence': 0,
    'certificate': '',
    'license': 'AGPL-3',
    'depends': [
        'mistralai_connector',
        'product',
        'sale',
    ],
    'category': 'AI',
    'complexity': 'easy',
    'qweb': [
    ],
    'demo': [
    ],
    'images': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/prompt_templates.xml',
        'data/mistralai_completion_data.xml',
        'views/mistralai_product_result_views.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
