{
    'name': 'Marcadores de Produto (Inventário)',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Marcadores coloridos para produtos, com filtro e agrupamento no Inventário',
    'description': """
Marcadores de Produto
======================
Permite criar marcadores (tags) coloridos e associá-los aos produtos, para
filtrar e agrupar produtos por marcador nas telas do Inventário.

Funcionalidades
---------------
* Tela de gestão de marcadores: criar, editar e excluir
* Seleção de cor para cada marcador
* Campo de marcadores no formulário do produto
* Filtro e agrupamento por marcador na busca de produtos
""",
    'author': 'Sohome',
    'license': 'LGPL-3',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_marcador_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
}
