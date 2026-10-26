# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = ['sale.order', 'ninaad.portal.salesperson.mixin']
    _name = 'sale.order'

    user_id = fields.Many2one(
        'res.users',
        string="Salesperson",
        index=True,
        tracking=2,
        default=lambda self: self.env.user,
        domain=lambda self: self._get_portal_salesperson_domain(
            ['sales_team.group_sale_salesman']
        ),
    )
