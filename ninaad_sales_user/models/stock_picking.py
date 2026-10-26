# -*- coding: utf-8 -*-
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = ['stock.picking', 'ninaad.portal.salesperson.mixin']
    _name = 'stock.picking'

    user_id = fields.Many2one(
        'res.users',
        string="Responsible",
        tracking=True,
        domain=lambda self: self._get_portal_salesperson_domain(
            ['stock.group_stock_user']
        ),
    )
