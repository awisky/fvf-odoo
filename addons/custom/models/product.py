# © 2021 bloopark systems (<http://bloopark.de>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.osv import expression


def make_domain(domain_name, code):
    """
    This function builds a domain spliting the code by spaces
    """
    domain_code = [(domain_name, 'ilike', '%')]
    if code:
        i = code.find(' ')
        domain_code = []
        while i != -1:
            domain_code.append((domain_name, 'ilike', code[0:i]))
            code = code[i+1:]
            i = code.find(' ')
        domain_code.append((domain_name, 'ilike', code))
    return domain_code


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100,
                     name_get_uid=None):
        res = super(ProductProduct, self)._name_search(
            name,
            args,
            operator,
            limit,
            name_get_uid
        )

        domain = make_domain('name', name)

        products_new_search = self.search(domain)

        if type(res) == list:
            res = list(set(res + products_new_search.ids))

        return res
