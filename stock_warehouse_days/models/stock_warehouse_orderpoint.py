# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from datetime import datetime, timedelta



class StockOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    is_warehouse_days = fields.Boolean(string='Warehouse days rule', default=False)
    warehouse_days = fields.Integer(string='Warehouse days', help='Warehouse days to be calculated for reordering rules, based on the sales of the associated product')



    @api.model
    def update_orderpoint(self):

        current_date = str(datetime.now())[:10]
        current_date = datetime.strptime(current_date, "%Y-%m-%d")
        days = 0
        product_qty = 0 #quantity to be updated on reordering rules

        orderpoints = self.env['stock.warehouse.orderpoint'].search([('is_warehouse_days','=',True)]) #get all orderules with warehouse days rules
        if orderpoints:
            for o in orderpoints:
                if o.warehouse_days > 0:
                    limit_date = current_date - timedelta(days=o.warehouse_days)
                    sales = self.env['sale.order.line'].search([('product_id','=',o.product_id.id)])
                    for s in sales:
                        sale_date = datetime.strptime(s.order_id.confirmation_date, "%Y-%m-%d %H:%M:%S")
                        if sale_date >= limit_date:
                            product_qty += s.product_uom_qty #in case there no sales of the product, the reordering rules have 0 value.
                    o.product_min_qty = product_qty  # updating reordering rules
                    o.product_max_qty = product_qty  # updating reordering rules
                    product_qty = 0
                    o.product_id.message_post(body=_('A reordering rule associated to this product has been updated. %s') % (o.name ))


