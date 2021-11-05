# -*- coding: utf-8 -*-
from odoo import http

# class RmaStatus(http.Controller):
#     @http.route('/wb_rma_status/wb_rma_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wb_rma_status/wb_rma_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wb_rma_status.listing', {
#             'root': '/wb_rma_status/wb_rma_status',
#             'objects': http.request.env['wb_rma_status.wb_rma_status'].search([]),
#         })

#     @http.route('/wb_rma_status/wb_rma_status/objects/<model("wb_rma_status.wb_rma_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wb_rma_status.object', {
#             'object': obj
#         })