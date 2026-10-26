# Portal User Salesperson

## Overview

**Portal User Salesperson** is an Odoo 18.0 module that lets Portal users be selected as the **Salesperson / Responsible** on records.

By default, Odoo allows only internal users from specific groups in this field, so Portal users never appear in the dropdown. This module adds Portal users to the selection. No extra setting is needed.

---

## Features

- Portal users can be selected as Salesperson / Responsible, in addition to the existing internal users.
- Works on **Contacts**, **Sale Orders**, **CRM Leads / Opportunities**, **Purchase Orders** and **Inventory Transfers**.
- Internal users from the existing groups stay selectable. Nothing is removed.
- Invoices and bills are not changed by this module.
- Only changes who can be selected. It does not grant portal users any extra access.

---

## Where It Applies

| Model | Field |
| --- | --- |
| Contacts (`res.partner`) | Salesperson |
| Sale Order (`sale.order`) | Salesperson |
| CRM Lead / Opportunity (`crm.lead`) | Salesperson |
| Purchase Order (`purchase.order`) | Purchase Representative |
| Inventory Transfer (`stock.picking`) | Responsible |

---

## Installation

1. Copy the module folder into your Odoo addons path.
2. Restart the Odoo server.
3. Go to **Apps**, click **Update Apps List**.
4. Search for **Portal User Salesperson** and click **Install**.

---

## Usage

1. Open a Sale Order, CRM Lead / Opportunity, Contact, Purchase Order or Inventory Transfer.
2. Click the Salesperson / Responsible field. Portal users are listed with the internal users.
3. Select a portal user.

**Note:** selecting a portal user does not change what that user can open. Access is still controlled by the existing access rights and record rules.

---

## Support

For support, contact: support@ninaadglobal.com

---

## Author

**Ninaad Global Pvt Ltd.**
https://www.ninaadglobal.com
