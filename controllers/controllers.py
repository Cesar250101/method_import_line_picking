# -*- coding: utf-8 -*-
from odoo import http

# class MethodImportLinePicking(http.Controller):
#     @http.route('/method_import_line_picking/method_import_line_picking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_import_line_picking/method_import_line_picking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_import_line_picking.listing', {
#             'root': '/method_import_line_picking/method_import_line_picking',
#             'objects': http.request.env['method_import_line_picking.method_import_line_picking'].search([]),
#         })

#     @http.route('/method_import_line_picking/method_import_line_picking/objects/<model("method_import_line_picking.method_import_line_picking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_import_line_picking.object', {
#             'object': obj
#         })