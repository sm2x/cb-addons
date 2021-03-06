# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    careplan_id = fields.Many2one(
        'medical.careplan',
        readonly=True,
    )
    procedure_request_id = fields.Many2one(
        'medical.procedure.request',
        readonly=True,
    )
    request_group_id = fields.Many2one(
        'medical.request.group',
        readonly=True,
    )
    medication_request_id = fields.Many2one(
        'medical.medication.request',
        readonly=True,
    )
    encounter_id = fields.Many2one(
        'medical.encounter',
        readonly=True,
    )
    document_reference_id = fields.Many2one(
        'medical.document.reference',
        readonly=True,
    )
    laboratory_request_id = fields.Many2one(
        'medical.laboratory.request', readonly=True,
    )
    laboratory_event_id = fields.Many2one(
        'medical.laboratory.event', readonly=True,
    )
    authorization_status = fields.Selection([
        ('pending', 'Pending authorization'),
        ('not-authorized', 'Not authorized'),
        ('authorized', 'Authorized'),
    ], readonly=True,)
