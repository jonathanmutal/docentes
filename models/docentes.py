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
from odoo.exceptions import UserError, ValidationError

from . import cargos
# from . import aportes
import time


STATE = [
    ('none', 'No afiliado'),
    ('hist', 'Histórico'),
    ('baja', 'Desafiliado'),
    ('pend_b', 'Pendiente de baja'),
    ('pend_a', 'Pendiente de alta'),
    ('pasivo', 'No cotizante'),
    ('jub', 'Jubilado'),
    ('juba', 'Jubilado Activo'),
    ('activo', 'Activo')
]

TIPODOC = [('dni','DNI'),('lc','LC'),('le','LE'),('pas','PAS'),('ci','CI')]
ESTCIV = [('c', 'Casada/o'),('s','Soltera/o'), ('u', 'Unida/o'),('v', 'Viuda/o'),('d', 'Divorciada/o'),('p','Separada/o'),('n','No sabe/No contesta')]
SEXO = [('f', 'Femenino'),('m','Masculino'), ('o', 'Otro'),('n','No sabe/No contesta')]




class Partner(models.Model):
    '''Partner'''
    _inherit = 'res.partner'
    _sql_constraints = [
        ('legajo',
        'unique(legajo)',
        'Este legajo ya existe! Por favor escriba nuevamente el legajo.'
         )
    ]


    cargos = fields.One2many('docentes.cargos', 'partner_id', 'Cargos')
    # aportes = fields.One2many('docentes.aportes', 'partner_id', 'Aportes')
    email2 = fields.Char('Otro Email', size=240)
    esdocente = fields.Boolean('Es docente?', default=False)
    legajo = fields.Integer('Legajo')
    tipodni = fields.Selection(TIPODOC,'Tipo doc')
    dni = fields.Integer('N documento')
    estadocivil = fields.Selection(ESTCIV,'Estado civil')
    sexo = fields.Selection(SEXO,'Sexo')
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    pais = fields.Many2one('res.country','País de nacimiento')
    afiliado = fields.Integer('N afiliado')
    afiliados_ant = fields.Char('N afiliado anteriores',size=240)
    fecha_alta = fields.Date('Fecha de alta')
    fecha_baja = fields.Date('Fecha de baja')
    antiguedad = fields.Date('Antigüedad')
    estado = fields.Selection(STATE,'Estado de afiliación')
    observado = fields.Boolean('Observado?')
    observacion = fields.Char('Observación', size=240)

    @api.multi
    def funcionSolicitarAfiliacion(self):
      today = time.strftime('%Y-%m-%d')
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado':'pend_a','fecha_alta': today})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi
    def funcionSolicitarDesafiliacion(self):
      today = time.strftime('%Y-%m-%d')
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado':'pend_b','fecha_baja': today})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi
    def funcionConfirmarAfiliacion(self):
      # El método self.write actualiza el campo en la interfaz

      reads = self.read(['afiliados_ant', 'afiliado'])
      for record in reads:
            afil = str(record['afiliado'])
            if record['afiliados_ant']:
                afil = record['afiliados_ant'] + ', ' + afil
           
      self.write({'estado': 'activo','afiliados_ant': afil})
      return True # Siempre tenemos que retornar True al final de la declaración
    
    @api.multi
    def funcionConfirmarDesafiliacion(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'baja'})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi 
    def funcionActivoaPasivo(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'pasivo'})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi
    def funcionActivoaJubilado(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'jub'})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi
    def funcionPasivoaActivo(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'activo'})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi 
    def funcionPasivoaHistorico(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'hist'})
      return True # Siempre tenemos que retornar True al final de la declaración
    
    @api.multi 
    def funcionJubiladoaHistorico(self):
      # El método self.write actualiza el campo en la interfaz
      self.write({'estado': 'hist'})
      return True # Siempre tenemos que retornar True al final de la declaración

    @api.multi
    def funcionJubiladoaCotizante(self):
      self.write({'estado': 'juba'})
      return True

    @api.multi
    def funcionJubiladoaNoCotizante(self):
      self.write({'estado': 'jub'})
      return True

    @api.multi
    def funcionPasivoaCotizante(self):
      self.write({'estado': 'activo'})
      return True

    @api.multi
    def funcionJubilar(self):
      self.write({'estado':'jub'})
      return True

    @api.multi
    def funcionAfiladoaNoCotizante(self):
      self.write({'estado':'pasivo'})
      return True

#Partner()
