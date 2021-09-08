# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    item_count = fields.Integer(compute='_compute_items', string='Items')

    city = fields.Char(related='partner_id.city', store=True)

    @api.depends('order_line')
    def _compute_items(self):
        for sale in self:
            sale.item_count = len(sale.order_line)

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


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    item_number = fields.Integer(compute='_compute_item_number', string='Seq')
    check = fields.Boolean()

    @api.depends('sequence')
    def _compute_item_number(self):
        for line in self:
            line.item_number = line.sequence - 9
