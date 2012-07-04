# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2011 Vianney da Costa - Akretion                                #
#               2012 Raphaël Valyi - Akretion
#                                                                               #
#This program is free software: you can redistribute it and/or modify           #
#it under the terms of the GNU General Public License as published by           #
#the Free Software Foundation, either version 3 of the License, or              #
#(at your option) any later version.                                            #
#                                                                               #
#This program is distributed in the hope that it will be useful,                #
#but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#GNU General Public License for more details.                                   #
#                                                                               #
#You should have received a copy of the GNU General Public License              #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.          #
#################################################################################


{
    'name': 'ooornithorinchus: OpenBravo POS for OpenERP',
    'version': '0.2',
    'category': 'Sales Management',
    'description': """
    Integration of the Point of Sale OpenBravo POS
    """,
    'author': 'Akretion',
    'complexity': "hard",
    'website': 'http://www.akretion.com',
    'depends': [
            'base_external_referentials',
            'kettle_connector',
            'product'
    ],
    'init_xml': [],
    'update_xml': [
          'settings/external.referential.type.csv',
          'settings/openbravopos1000/external.referential.version.csv',
          'settings/openbravopos1000/external.mapping.template.csv',
          'external_referentials_view.xml',
          'product_view.xml'
    ],
    'test': [],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
