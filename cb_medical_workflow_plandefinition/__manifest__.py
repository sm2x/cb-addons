# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Plan Definition',
    'version': '11.0.1.0.0',
    'author': 'Eficent, Creu Blanca, Odoo Community Association (OCA)',
    'depends': [
        'medical_clinical_request_group',
        'medical_clinical_procedure',
        'medical_administration_encounter_careplan',
        'medical_document',
        'medical_clinical_laboratory',
        'cb_medical_administration_center',
    ],
    'data': [
        'views/workflow_activity_definition.xml',
        'views/workflow_plan_definition_action.xml',
        'views/workflow_plan_definition.xml',
        'views/medical_request_views.xml',
    ],
    'website': 'https://github.com/OCA/vertical-medical',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
