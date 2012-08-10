# -*- coding: utf-8 -*-
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
from base_external_referentials.external_osv import ExternalSession

class product_product(osv.osv):
    _inherit = "product.product"

    _columns = {
        'barcode':fields.char('Barcode', size=64),
    }

    def get_ids_and_update_date_rpc(self, cr, uid, shop_id, ids=None, last_exported_date=None, context=None):
        shop = self.pool.get('sale.shop').browse(cr, uid, shop_id)
        referential = shop.referential_id
        external_session = ExternalSession(referential, shop)
        return self.get_ids_and_update_date(cr, uid, external_session, ids, last_exported_date, context)


def get_modified_ids(self, cr, uid, date=False, context=None): 
    """ This function will return the ids of the modified or created items of self object since the date

    @return: a table of this format : [[id1, last modified date], [id2, last modified date] ...] """
    if date:
        sql_request = "SELECT id, create_date, write_date FROM %s " % (self._name.replace('.', '_'),)
        sql_request += "WHERE create_date > %s OR write_date > %s;"
        cr.execute(sql_request, (date, date))
    else:
        sql_request = "SELECT id, create_date, write_date FROM %s " % (self._name.replace('.', '_'),)
        cr.execute(sql_request)
    l = cr.fetchall()
    res = []
    for p in l:
        if p[2]:
            res += [[p[0], p[2]]]
        else:
            res += [[p[0], p[1]]]
    return sorted(res, key=lambda date: date[1])

osv.osv.get_modified_ids = get_modified_ids

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
