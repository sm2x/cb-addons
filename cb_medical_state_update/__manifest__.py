# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Medical Update State of requests',
    'version': '11.0.1.0.0',
    'author': 'Eficent, Creu Blanca, Odoo Community Association (OCA)',
    'category': 'Medical',
    'depends': [
        'medical_workflow',
        'medical_administration_encounter_careplan',
        'medical_clinical_procedure',
        'medical_clinical_request_group',
        'medical_document',
        'medical_medication_request',
        'cb_medical_careplan_sale',
        'cb_medical_workflow_trigger',
    ],
    'data': [
    ],
    'website': 'https://github.com/eficent/cb-addons',
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
