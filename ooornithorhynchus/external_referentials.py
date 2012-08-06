# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
# Copyright (C) 2011 Vianney da Costa - Akretion                                #
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

from osv import osv
from osv import fields

class external_mapping(osv.osv):
    _inherit = 'external.mapping'
    
    _columns = {
        'last_import_date':fields.datetime('Last Import Date'),
        'last_export_date':fields.datetime('Last Export Date')
    }

external_mapping()

class external_referential(magerp_osv.magerp_osv):
    _inherit = "external.referential"

    @only_for_referential('openbravopos')
    def external_connection(self, cr, uid, id, debug=False, logger=False, context=None):
        return None

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
