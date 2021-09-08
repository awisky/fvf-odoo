# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)


class PriceUpdate(models.TransientModel):
    """
    """
    _name = "price.update"
    _description = "Price Update"

    line_ids = fields.One2many(
        'price.update.line', 'wizard_id')
    selected = fields.Boolean('', default=True)

    def _search(self):
        self.line_ids = False

        active_id = self._context.get('active_id', False)
        sale_obj = self.env['sale.order']
        sale = sale_obj.browse(active_id)
        selected = self.selected
        line_ids = []
        if sale:

            for line in sale.order_line:

                line_ids.append((0, 0, {
                    'selected': selected,
                    'line_id': line.id,
                    'product_id': line.product_id.id,
                    'product_uom': line.product_uom.id,
                    'current_price': line.product_id.list_price,
                    'price_unit': line.price_unit or 0.0
                }))

            self.line_ids = line_ids

    @api.onchange('selected')
    def search(self):
        """
        """
        self._search()

    def update_quotation_price(self):
        for search_wizard in self:
            selection = [
                line for line in search_wizard.line_ids if line.selected]
            if len(selection) > 0:
                for line in search_wizard.line_ids:
                    if line.selected:
                        line.line_id.update({'price_unit': line.current_price})
        return {'type': 'ir.actions.act_window_close'}

    def update_product_price(self):
        for search_wizard in self:
            selection = [
                line for line in search_wizard.line_ids if line.selected]
            if len(selection) > 0:
                for line in search_wizard.line_ids:
                    if line.selected:
                        line.product_id.list_price = line.price_unit
        return {'type': 'ir.actions.act_window_close'}


class PriceUpdateLine(models.TransientModel):
    """
    """
    _name = "price.update.line"
    _description = "Price Update Line"

    wizard_id = fields.Many2one('price.update', string='Search')
    selected = fields.Boolean(string='')
    product_id = fields.Many2one('product.product')
    line_id = fields.Many2one('sale.order.line')
    product_uom = fields.Many2one('uom.uom')
    current_price = fields.Float(digits='Product Price', default=0.0)
    price_unit = fields.Float(digits='Product Price', default=0.0)
