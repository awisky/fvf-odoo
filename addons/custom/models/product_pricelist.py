
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from dateutil.relativedelta import relativedelta
from odoo import fields, models, api, _
from odoo.tools import date_utils
from odoo.exceptions import ValidationError


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    product_uom = fields.Many2one('uom.uom')
