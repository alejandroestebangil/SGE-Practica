from odoo import api, models, fields

class Tienda(models.Model):
    """Modelo para la tabla 'charcuteria.tienda'"""

    _name = 'charcuteria.tienda'
    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Direccion', required=True)
    telefono = fields.Char(string='Telefono')
    embutido_id = fields.Many2many(comodel_name='charcuteria.embutido', inverse_name='tienda_id')

class Embutido(models.Model):
    """Modelo para la tabla 'charcuteria.embutido'"""

    _name = 'charcuteria.embutido'
    tipo = fields.Selection([('chorizo', 'Chorizo'),
                            ('salchichon', 'Salchichon'),
                            ('jamon', 'Jamon'),
                            ('lomo', 'Lomo'),
                            ('salami', 'Salami')],
                            string='Embutido', required=True)
    precio = fields.Float(string='Precio', required=True)
    tienda_id = fields.Many2many(comodel_name='charcuteria.tienda', inverse_name='embutido_id')
    