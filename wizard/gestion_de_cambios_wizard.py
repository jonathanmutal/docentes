from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from odoo.addons.docentes.config.config import *


class DocentesGestionDeCambioWiz(models.TransientModel):
    _name ='docentes.gestion.wizard'

    fecha_desde = fields.Datetime('Fecha desde',
                           help="Elegir desde la fecha",
                           default=fields.Datetime.now(),
                           required=True)
    fecha_hasta = fields.Datetime('Fecha hasta',
                           help="Elegir hasta fecha para mostrar los socios",
                           default=fields.Datetime.now(),
                           required=True)


    @api.multi
    @api.depends('fecha_desde', 'fecha_hasta')
    def set_situacion(self):
        aportes = self.env['docentes.aportes'].search([('fecha', '>=', self.fecha_desde), ('fecha', '<=', self.fecha_hasta)])
        if not aportes:
            raise UserError("No hay aportes entre esas fechas")

        docentes_situacion = []
        docentes = self.env['res.partner'].search([('esdocente', '=', True)])
        for docente in docentes:
            aporte_docente = aportes.search([('docente.id', '=', docente.id)])
            if not aporte_docente:
                situacion = DOCENTE_NO_APORTO.get(docente.estado, OT)
                docente_aporte = {
                    'docente': docente.id,
                    'situacion': situacion,
                    'fecha': None
                }
                docentes_situacion.append(docente_aporte)
            else:
                for aporte in aporte_docente:
                    situacion = DOCENTE_APORTO.get(docente.estado, ACTIVO)
                    if situacion == ACTIVO:
                        continue
                    docente_aporte = {
                        'docente': docente.id,
                        'situacion': situacion,
                        'fecha_de_aporte': aporte.fecha
                    }
                    docentes_situacion.append(docente_aporte)

        if not docentes_situacion:
            raise UserError("No hay docentes con posibles cambios entre esas fechas")

        docentes_cambio = []
        for docente in docentes_situacion:
            ## Agregamos los dos ceros primeros para que se cree el docenteGestionCambios
            d_cambio = (0, 0, docente)
            docentes_cambio.append(d_cambio)

        nueva_gestion = {
            'docentes_cambio': docentes_cambio,
            'fecha_desde': self.fecha_desde,
            'fecha_hasta': self.fecha_hasta
        }
        id_ge = self.env['docentes.gestion_de_cambios.modelo'].create(nueva_gestion)

        return {
            'type': 'ir.actions.act_window',
            'name': 'Gestión de cambios',
            'res_model': 'docentes.gestion_de_cambios.modelo',
            'res_id': id_ge.id,
            # 'taget': 'new',
            'view_mode': 'form',
            'view_type': 'form'
        }
