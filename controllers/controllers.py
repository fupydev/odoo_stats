# -*- coding: utf-8 -*-
# from odoo import http


# class CodStatv1(http.Controller):
#     @http.route('/cod_statv1/cod_statv1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cod_statv1/cod_statv1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cod_statv1.listing', {
#             'root': '/cod_statv1/cod_statv1',
#             'objects': http.request.env['cod_statv1.cod_statv1'].search([]),
#         })

#     @http.route('/cod_statv1/cod_statv1/objects/<model("cod_statv1.cod_statv1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cod_statv1.object', {
#             'object': obj
#         })
