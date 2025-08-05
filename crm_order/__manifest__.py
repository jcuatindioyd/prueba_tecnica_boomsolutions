{
    'name': "Crm Order",
    'category': 'CRM',
    'summary': "Allows you to record the date and user who approves the order.",
    'version': '2.0',
    'depends': ['crm'],
    'data': [
        'data/crm_lead.xml',
        'views/crm_order_views.xml',
    ],
    "installable": True,
    'license': 'LGPL-3',
}