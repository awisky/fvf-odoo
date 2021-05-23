# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Custom',
    'version': '14.0.0.0',
    'category': 'Sales',
    'summary': "FVF Customizations",
    'author': 'Agustin Wisky',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'product',
        'sale_stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/sale_report_templates.xml',
        'report/sale_report.xml',
        'views/sale_order_view.xml',
        'views/product_pricelist_view.xml',
        'wizard/price_update_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
