# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = ['res.partner', 'ninaad.portal.salesperson.mixin']
    _name = 'res.partner'

    user_id = fields.Many2one(
        'res.users',
        string="Salesperson",
        domain=lambda self: self._get_portal_salesperson_domain(
            ['sales_team.group_sale_salesman']
        ),
    )
