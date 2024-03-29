# Copyright (C) 2024 - Michel Perrocheau (https://github.com/myrrkel).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/algpl.html).
{
    'name': 'Mistral AI Chat',
    'version': '16.0.0.0.1',
    'author': 'Michel Perrocheau',
    'website': 'https://github.com/myrrkel',
    'summary': "Add a Mistral AI Bot user to chat with",
    'sequence': 0,
    'certificate': '',
    'license': 'AGPL-3',
    'depends': [
        'mistralai_connector',
        'mail',
        'bus',
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
        'data/mistralai_chat_data.xml',
        'data/mistralai_completion_data.xml',
    ],
    'assets': {
        'mail.assets_messaging': [
            'mistralai_chat/static/src/models/messaging_initializer.js',
        ],
    },
    'auto_install': False,
    'installable': True,
    'application': False,
}
