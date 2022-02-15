{
    'name': "Hospital Module",
    'summary': "Odoo lap-1 Task",
    'discription': """
        This module is created as the 1st day task of Odoo course
    """,
    'author':"ab-gad",
    'website':"https://github.com/ab-gad",
    'catigory': "uncatigorised",
    'version': "0.1",
    
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_view.xml',
        'views/hms_departments_view.xml',
        'views/doctor_view.xml',
        'views/crm_inherited_view.xml',
        'reports/report.xml',
        'reports/template.xml',
        ],

    'depends': ['crm'],
}