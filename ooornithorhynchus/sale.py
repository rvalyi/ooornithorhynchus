    # -*- encoding: utf-8 -*-
#########################################################################
#                                                                       #
# Copyright (C) 2012  Raphaël Valyi - Akretion                          #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################

from osv import osv, fields
from base_external_referentials.external_osv import ExternalSession

class sale_order(osv.osv):
    _inherit = "sale.order"

    def pay_and_update_rpc(self, cr, uid, shop_id, order_id, resource, context=None):
        shop = self.pool.get('sale.shop').browse(cr, uid, shop_id)
        referential = shop.referential_id
        external_session = ExternalSession(referential, shop)
        order = self.browse(cr, uid, order_id)
        resource = {'payment': {'amount_paid': order.amount_total}}
        return self.paid_and_update(cr, uid, external_session, order_id, resource, context)

