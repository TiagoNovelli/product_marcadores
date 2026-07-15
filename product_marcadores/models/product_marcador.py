from odoo import fields, models


class ProductMarcador(models.Model):
    _name = 'product.marcador'
    _description = 'Marcador de Produto'
    _order = 'name'

    name = fields.Char(string='Nome', required=True, translate=True)
    color = fields.Integer(string='Cor')
    active = fields.Boolean(string='Ativo', default=True)
    product_tmpl_ids = fields.Many2many(
        'product.template',
        relation='product_marcador_product_template_rel',
        string='Produtos',
    )
    product_count = fields.Integer(string='Produtos', compute='_compute_product_count')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Já existe um marcador com este nome!'),
    ]

    def _compute_product_count(self):
        for marcador in self:
            marcador.product_count = len(marcador.product_tmpl_ids)
