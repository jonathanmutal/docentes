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


{
    'name': 'Docentes',
    'version': '2.1.9',
    'category': 'Asociacion',
    'summary': """Docentes y Afiliados""",

    'description': """
Este módulo permite gestionar Docentes y Afiliados de una asociación.
=========================================================================

Incorpora nueva información a la categoría Partner y menúes específicos para filtar la información. 
    """,
    'author': "Araceli Acosta y Jonathan Mutal",
    'depends': ['base'],
    'data': [
        'security/docentes_security.xml',
        'views/docentes_cargos_tipo_view.xml',
        'views/docentes_cargos_view.xml',
        'views/docentes_view.xml',
        'views/docentes_mails_view.xml',
        'views/aportes_view.xml',
        'views/gestion_de_cambios_view.xml',

        'wizard/gestion_de_cambios_wizard_view.xml'
    ],
    'application': True,
}

