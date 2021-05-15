# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def call_price_update_assistant(self):

        return {
            'name': _("Price Update"),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'price.update',
            'context': {'active_model': 'sale.order'},
            'active_id': self.id,
            'target': 'new',
        }


