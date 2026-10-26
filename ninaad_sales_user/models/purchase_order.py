# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = ['purchase.order', 'ninaad.portal.salesperson.mixin']
    _name = 'purchase.order'

    user_id = fields.Many2one(
        'res.users',
        string="Purchase Representative",
        index=True,
        tracking=True,
        default=lambda self: self.env.user,
        domain=lambda self: self._get_portal_salesperson_domain(
            ['purchase.group_purchase_user']
        ),
    )
