{
    'name': 'Runbot',
    'category': 'Website',
    'summary': 'Runbot',
    'version': '1.2',
    'description': "Runbot",
    'author': 'OpenERP SA',
    'depends': ['base_setup', 'website'],
    'external_dependencies': {
        'python': ['matplotlib'],
    },
    'data': [
        'views/runbot_backend.xml',
        'views/runbot_templates.xml',
        'views/res_config_view.xml',
        'security/runbot_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
    ],
    'installable': True,
}
