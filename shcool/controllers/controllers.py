# -*- coding: utf-8 -*-
from odoo import http

# class Shcool(http.Controller):
#     @http.route('/shcool/shcool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shcool/shcool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shcool.listing', {
#             'root': '/shcool/shcool',
#             'objects': http.request.env['shcool.shcool'].search([]),
#         })

#     @http.route('/shcool/shcool/objects/<model("shcool.shcool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shcool.object', {
#             'object': obj
#         })