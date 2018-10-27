from odoo import api, fields, models, _
from odoo.addons.docentes.config.config import SITUACION

class DocentesGestionDeCambio(models.Model):
    _name = 'docentes.gestion_de_cambios'
    _order = 'fecha_de_aporte desc, docente, situacion'

    docente = fields.Many2one('res.partner', 'Docente',
                                 required=True,
                                 ondelete='cascade',
                                 readonly=True
                                 )
    gestion = fields.Many2one('docentes.gestion_de_cambios.modelo',
                                 string='Lista de cambios',
                                 readonly=True,
                                 ondelete='set null')
    fecha_de_aporte = fields.Date('Fecha de aporte')
    situacion = fields.Selection(SITUACION, 'Situación actual', readonly=True)

    @api.multi
    def crearDocente(self):
        id_docente = self.docente.id
        self.docente.update({'esdocente': True})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Gestión de cambios',
            'res_model': 'res.partner',
            'res_id': id_docente,
            # 'taget': 'new',
            'view_mode': 'form',
            'view_type': 'form'
        }



class GestionDeCambio(models.Model):
    _name ='docentes.gestion_de_cambios.modelo'
    _order = 'fecha_desde desc,fecha_hasta desc'
    _description = 'Tabla de gestión de cambios'
    _sql_constraints = [
        ('fechas',
        'unique(fecha_desde, fecha_hasta)',
        'Estas fechas ya existen!' \
        'Si quiere realizar nuevamente una consulta para gestión de cambio,' \
        'por favor borre la anterior.'
         )
    ]

    docentes_cambio = fields.One2many('docentes.gestion_de_cambios',
                             'gestion',
                             string='Lista de cambios',
                             readonly=True)
    fecha_desde = fields.Date('Fecha desde',
                                  readonly=True)
    fecha_hasta = fields.Date('Fecha hasta',
                                  readonly=True)
