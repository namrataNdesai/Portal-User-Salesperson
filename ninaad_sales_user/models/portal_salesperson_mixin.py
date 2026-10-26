# -*- coding: utf-8 -*-
from odoo import models


class PortalSalespersonMixin(models.AbstractModel):
    """Shared helper: builds a domain that keeps the original allowed
    internal group(s) for a Salesperson/Responsible field and ALSO allows
    Portal users, without opening the field to every res.users record
    (e.g. the technical "Public User" stays excluded).
    """
    _name = 'ninaad.portal.salesperson.mixin'
    _description = 'Portal Salesperson Domain Mixin'

    def _get_portal_salesperson_domain(self, extra_group_xmlids=None):
        """
        :param extra_group_xmlids: list of external ids of the internal
            group(s) that should remain allowed for this particular field
            (e.g. sales_team.group_sale_salesman for sale.order,
            purchase.group_purchase_user for purchase.order, ...).
        """
        group_ids = []
        for xmlid in (extra_group_xmlids or []):
            group = self.env.ref(xmlid, raise_if_not_found=False)
            if group:
                group_ids.append(group.id)

        portal_group = self.env.ref('base.group_portal', raise_if_not_found=False)
        if portal_group:
            group_ids.append(portal_group.id)

        return [('groups_id', 'in', group_ids)] if group_ids else []
