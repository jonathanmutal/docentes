from odoo import api, fields, models, _


SITUACION = [
    ('ASD', 'Activo sin descuentos'),
    ('PSD', 'Pendiente de alta sin descuentos'),
    ('OT', 'Otra situación')
]


class DocentesGestionDeCambio(models.Model):
    _name = 'docentes.gestion_de_cambios'
    _order = 'situacion'

    docente = fields.Many2one('res.partner', 'Docente',
                                 required=True,
                                 ondelete='cascade',
                                 readonly=True)
    gestion = fields.Many2one('docentes.gestion_de_cambios.modelo',
                                 string='Lista de cambios',
                                 readonly=True,
                                 ondelete='cascade')
    situacion = fields.Selection(SITUACION, 'Situación actual', readonly=True)


class GestionDeCambio(models.Model):
    _name ='docentes.gestion_de_cambios.modelo'
    _order = 'titulo desc,fecha_desde desc'
    _description = 'Tabla de gestión de cambios'
    _sql_constraints = [
        ('titulo',
        'unique(titulo)',
        'Seleccionar otro nombre para gestión de cambio. Este ya existe!'
         )
    ]

    titulo = fields.Char(string='Nombre de gestión de cambio')
    docentes_cambio = fields.One2many('docentes.gestion_de_cambios',
                             'gestion',
                             string='Lista de cambios',
                             readonly=True)
    fecha_desde = fields.Datetime('Fecha desde',
                                  readonly=True)
    fecha_hasta = fields.Datetime('Fecha hasta',
                                  readonly=True)
