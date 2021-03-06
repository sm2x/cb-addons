# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class MedicalCareplanAddPlanDefinition(models.TransientModel):
    _inherit = 'medical.careplan.add.plan.definition'

    def _get_values(self):
        values = super(MedicalCareplanAddPlanDefinition, self)._get_values()
        values['sub_payor_id'] = self.careplan_id.sub_payor_id.id
        return values
