# -*- coding: utf-8 -*-
##############################################################################
#
#    Módulo Docentes para Odoo
#    Copyright (C) Araceli Acosta.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from odoo import api, fields, models, _
from odoo.addons.docentes.config.config import *

import time


class DocentesAportes(models.Model):
    '''Aportes de docentes afiliados'''
    _name = 'docentes.aportes'
    _order = 'fecha desc, nombre'
    _description = 'Modelo para los aportes'

    docente = fields.Many2one('res.partner',
        string='Docente',
        required=True,
        ondelete='cascade')
    legajo = fields.Integer('Legajo', required=True)
    nombre = fields.Char('Nombre', size=30)
    fecha = fields.Date('Fecha', default=fields.Datetime.now(), required=True)
    codigo = fields.Integer('Codigo')
    aporte = fields.Float('Aporte',
        digits=(16,2),
        required=True,
        store=True)

    @api.multi
    @api.depends('legajo', 'nombre')
    def create(self, vals):
        """
        Override the create's method
        """
        legajo = vals['legajo']
        nombre = vals['nombre']
        docente = self.env['res.partner'].search([('legajo', '=', legajo)])
        if not docente:
            nuevo_docente = {
                'legajo': legajo,
                'name': nombre,
                'esdocente': True,
                'estado': NONE
            }
            docente = self.env['res.partner'].create(nuevo_docente)
            self.env['docentes.gestion_de_cambios'].create({
                'fecha_de_aporte': vals['fecha'] if 'fecha' in vals else fields.Datetime.now(),
                'docente': docente.id,
                'situacion': NOA
                })

        vals.update({
            'docente': docente.id,
            'aporte': vals['aporte'] / 100
            })

        return super(DocentesAportes, self).create(vals)
