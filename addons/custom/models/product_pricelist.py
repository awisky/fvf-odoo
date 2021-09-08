
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    product_uom = fields.Many2one('uom.uom')
