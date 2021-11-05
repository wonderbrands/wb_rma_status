# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError, AccessError
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, time
from odoo.tools import email_re, email_split
from odoo.tools.translate import _
from lxml import etree
from io import StringIO, BytesIO

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rma_check = fields.Selection([('00','Devuelto'),
                                  ('01','Sin cambios'),],
                                  string='RMA Estatus', compute='_rma_status')
    #contador = fields.Integer(string='Contador', track_visibility='onchange')

    @api.one
    def _rma_status(self):
        self.ensure_one()

        #for each in self:
        rma = self.env['crm.claim.ept'].search([('picking_id.sale_id', '=', self.id)])
        count = len(rma)

        if count != 0:
            self.rma_check = '00'