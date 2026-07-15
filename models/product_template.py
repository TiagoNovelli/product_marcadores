from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    marcador_ids = fields.Many2many(
        'product.marcador',
        relation='product_marcador_product_template_rel',
        string='Marcadores',
    )
