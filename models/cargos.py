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



CARACTER = [('INTE','Docente Interino'),('INTC','Interino Reemplazo con goce'),('INTS','Interino Reemplazo sin goce'),('CONC','Docente Concurso'),('NIVM','Docente Nivel Medio'),('TICV','Titular c/Vencimiento'),('TISV','Titular s/Vencimiento'),('INTW','Docente Interino en Comisión'),('TCVW','Titular Con vencimiento en comisión'),('TSVW','Titular sin vencimiento en comisión')]
TIPOLIC  = [('011', 'Licencia Docente por Beca (Ord. 1/91 – Art. 1°)'),('031', 'Licencia Docente por Congresos (Ord. 1/91 – Art. 3°)'),('041a', 'Licencia Docente para Trabajo Científico (Ord.1/91- Art.4° Inc. a)'),
	    ('041b', 'Licencia Docente para Trabajo Científico (Ord. 1/91- Art.4° Inc. b)'),('041c', 'Licencia Docente para Trabajo Científico (Ord. 1/91- Art. 4o -Inc c)'),
	    ('051', 'Licencia Docente para Doctorarse (Ord. 1/91 – Art. 5°)'),('061', 'Licencia Docente para Funciones Cient.-Téc. en la Provincia (Ord. 9/97)'),
	    ('071a', 'Licencia Docente por Causas no Previstas en Ord. 1/91 (Art.12)'),('071b', 'Licencia Docente por Causas no Previstas en Ord. 1/91 (Art.12)'),
	    ('091a', 'Licencia Anual (Art. 9)– días hábiles(ND)'),('091d','Licencia Anual Docente'),('101', 'Enfermedad de Corto Tratamiento (Art.10-a)'),('102a', 'Enfermedad de Largo Tratamiento (Art.10-c)'),('102b', 'Enfermedad de Largo Tratamiento (Art.10-c)'),
	    ('102c', 'Enfermedad de Largo Tratamiento (s.s) (Art.10-c)'),('102d', 'Inasistencia por Enfermedad sin certificado(Res. Rec. 1270/95)'),
	    ('103', 'Justificación de Inasistencia por Accidente de Trabajo (ART LEY 24557)'),('104a', 'Maternidad (Art. 10-g)'),('104b', 'Maternidad (Art. 10-g)'),
	    ('104c', 'Maternidad (Art. 10-g) Ley 24714-Res.14/02 de la Sec.Seg.Soc'),('104d', 'Maternidad (ley 24716)-Lic.para madres con hijos con Síndrome de Down'),('104t', 'Maternidad Lic.para madres con trillizos'),
	    ('105', 'Tenencia con Fines de Adopción (Art10-h)'),('106', 'Atención de Hijos Menores (Art. 10-i)'),('107a', ' Atención del Grupo Familiar (Art. 10-j)'),('107b', 'Atención del Grupo Familiar (s.s.) (Art. 10-j)'),
	    ('108', 'Enfermedad en Horas de Labor'),('109a', 'Incapacidad (Art.10)Tareas Livianas'),('109b', 'Reduccion Horaria y/o Tareas Livianas'),('130a', 'Para Rendir Exámenes (Art. 13-I-a)-28 días anuales-Nivel Terciario-Postgrado'),
	    ('130b', 'Para rendir Exámenes (Art. 13-a)-12 días anuales-Nivel Secundario'),('131', 'Para realizar Estudios o Investigaciones (Art. 13-I-b)'),('132', 'Para Estudios en la Escuela de Defensa Nacional (Art.13-I-c)'),
	    ('133a', 'Matrimonio del Agente (Art. 13-I-d)'),('133b', 'Matrimonio de Hijos de Agente (Art.13-I-d)'),('134a', 'Actividades Deportivas no Rentadas (Art.13-I-e ; Ley 20546)'),
	    ('134b', 'Actividades Deportivas no Rentadas (Art. 13,I-e ; Ley 20546)'),('135', 'Ejercicio Transitorio de Otros Cargos (Art. 13-II-a)'),('136', 'Razones Particulares (Art. 13-II-b)'),('137', 'Razones de Estudio (Art. 13-II-c)'),
	    ('138', 'Para Acompañar al Cónyuge (Art. 13-II-d)'),('139', 'Licencia por Cargo de Mayor Jerarquía (Art. 13-II-e)'),('141', 'Justificación por Nacimiento (Art. 14-a)'),('142a', 'Justificación por Fallecimiento (Art. 14-b)'),
	    ('142b', 'Justificación por Fallecimiento (Art. 14-b)'),('143', 'Justificación por Razones Especiales (Art. 14-c)'),('144', 'Justificación por Donación de Sangre (Art. 14-d)'),('145a','Justificación por Razones Particulares (Art. 14-f)'),
	    ('145b', 'Justificación por Razones Particulares (s.s.) (Art. 14-f)'),('145c', 'Injustificación de Inasistencias (Art. 14-f)'),('146', 'Para Integrar Mesas Examinadoras (Art. 14-g)'),('147', 'Exceso de Inasistencias (Art. 14-h)'),
	    ('150', 'Horario para Estudiantes (Art. 15-a)'),('151', 'Franquicia para Madre de Lactantes (Art. 15-b)'),('152', 'Franquicia para Asistencia a Congresos (Art. 15-c)'),('161', 'Receso Invernal'),('171a', 'Licencia Gremial'),
	    ('171b', 'Franquicia Gremial'),('181', 'Licencia por año sabatico'),('190', 'Paro gral de transporte(RR 128519/09/02)'),('200', 'Lic. Por invalidez provisoria'),
	    ('995', 'Sancion por Incumplimiento de Compromiso(Res.Rect. 1600/00 y 1122/01)'),('996', 'Supresion de cargo'),('997', 'Retencion de haberes'),('998', 'Sanciones'),('999', 'Reserva del cargo (para Esc. Sup. C. Manuel Belgrano)')]



class DocentesCargosTipo(models.Model):
    '''Tipo de cargo'''

    _name = 'docentes.cargos.tipo'
    _order = 'codigo'

    codigo = fields.Integer('Código',required=True)
    descripcion = fields.Char('Descripción',size=240,required=True)
    dedicacion = fields.Float('Horas dedicadas')
    horas_catedra = fields.Boolean('Horas cátedras')
    cargo_nomenclador = fields.Char('Cargo equivalente en nomenclador', size=240)

    @api.multi
    def name_get(self, context=None):
        if not ids:
            return []
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['codigo', 'descripcion'], context=context)
        res=[]
        for record in reads:
            name = record['descripcion']
            if record['codigo']:
                name = str(record['codigo']) + ' ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if context is None:
            context = {}
        ids = []
        #if context.get('journal_type', False):
            #args += [('type','=',context.get('journal_type'))]
        if name:
            ids = self.search(cr, user, [('codigo', 'ilike', name)] + args, limit=limit, context=context)
        if not ids:
            ids = self.search(cr, user, [('descripcion', 'ilike', name)] + args, limit=limit, context=context)#fix it ilike should be replace with operator

        return self.name_get(cr, user, ids, context=context)

#DocentesCargosTipo()


class DocentesCargos(models.Model):
    '''Cargos de docentes'''

    _name = 'docentes.cargos'
    _order = 'partner_id'

    partner_id = fields.Many2one('res.partner', 'Docente', required=True, select=True, ondelete='cascade')
    tipo_cargo = fields.Many2one('docentes.cargos.tipo','Categoría',required=True, select=True, ondelete='no action')
    horas = fields.Float('Cantidad de horas')
    dependencia = fields.Many2one('res.partner.category', 'Dependencia',required=True, select=True)
    caracter = fields.Selection(CARACTER, 'Caracter')
    fecha_alta = fields.Date('Fecha de alta')
    fecha_baja = fields.Date('Fecha de baja')
    licencia = fields.Boolean('De licencia')
    inicio_licencia = fields.Date('Inicio de licencia')
    fin_licencia = fields.Date('Fin de licencia')
    tipo_licencia = fields.Selection(TIPOLIC, 'Tipo de licencia')
