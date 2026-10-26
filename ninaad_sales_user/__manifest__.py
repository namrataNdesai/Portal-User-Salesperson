{
    'name': 'Portal User Salesperson',
    'version': '18.0.1.0.0',
    'summary': 'Allow Portal users to be selected as Salesperson/Responsible '
               'on Sale, CRM, Purchase, Inventory and Contacts',
    'description': """
Portal User Salesperson
=======================
By default Odoo restricts the "Salesperson" / "Responsible" (user_id) field
to internal users belonging to specific groups, so Portal users never appear
in the dropdown.

This module also allows Portal users to be selected in this field on:

    - Contacts                 (res.partner        -> user_id)
    - Sale Order               (sale.order          -> user_id)
    - CRM Lead / Opportunity   (crm.lead            -> user_id)
    - Purchase Order           (purchase.order      -> user_id)
    - Inventory Transfers      (stock.picking       -> user_id)

Internal users belonging to the relevant existing group(s) remain
selectable exactly as before - this module only ADDS Portal users as an
extra allowed option, it does not remove any existing permission.

Invoices and bills (account.move) are not changed by this module.

IMPORTANT: This only changes who can be PICKED in the field. It does NOT
by itself grant portal users extra read/write access to these records.
Access is still governed separately by ir.model.access.csv and ir.rule.
""",
    'category': 'Sales',
    'author': 'Ninaad Global Pvt Ltd.',
    'website': 'https://www.ninaadglobal.com',
    'support': 'support@ninaadglobal.com',
    'depends': [
        'sale_management',
        'contacts',
        'crm',
        'purchase',
        'stock',
    ],
    'data': [
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'images': ['static/description/screen_image.png'],
    'installable': True,
    'application': False,
    'license': 'Other proprietary',
}
