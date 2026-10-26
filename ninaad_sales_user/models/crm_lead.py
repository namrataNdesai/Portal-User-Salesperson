# -*- coding: utf-8 -*-
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = ['crm.lead', 'ninaad.portal.salesperson.mixin']
    _name = 'crm.lead'

    user_id = fields.Many2one(
        'res.users',
        string="Salesperson",
        index=True,
        tracking=True,
        default=lambda self: self.env.user,
        domain=lambda self: self._get_portal_salesperson_domain(
            ['sales_team.group_sale_salesman']
        ),
    )
