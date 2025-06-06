# -*- coding: utf-8 -*-
# from odoo import http


# class BaseQuickCount(http.Controller):
#     @http.route('/base_quick_count/base_quick_count', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/base_quick_count/base_quick_count/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('base_quick_count.listing', {
#             'root': '/base_quick_count/base_quick_count',
#             'objects': http.request.env['base_quick_count.base_quick_count'].search([]),
#         })

#     @http.route('/base_quick_count/base_quick_count/objects/<model("base_quick_count.base_quick_count"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('base_quick_count.object', {
#             'object': obj
#         })

