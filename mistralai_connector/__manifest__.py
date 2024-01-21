# Copyright (C) 2024 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Mistral AI Connector',
    'version': '16.0.0.0',
    'author': 'Michel Perrocheau',
    'website': 'https://github.com/myrrkel',
    'summary': "Connector for Mistral AI API",
    'sequence': 0,
    'certificate': '',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'external_dependencies': {
        'python': ['mistralai'],
    },
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
        'views/res_config_settings_views.xml',
        'views/mistralai_completion_views.xml',
        'views/mistralai_completion_result_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mistralai_connector/static/src/scss/style.scss',
        ],
    },

    'auto_install': False,
    'installable': True,
    'application': False,
}
