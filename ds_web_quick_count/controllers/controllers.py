# -*- coding: utf-8 -*-
# from odoo import http


# class WebQuickCount(http.Controller):
#     @http.route('/web_quick_count/web_quick_count', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_quick_count/web_quick_count/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_quick_count.listing', {
#             'root': '/web_quick_count/web_quick_count',
#             'objects': http.request.env['web_quick_count.web_quick_count'].search([]),
#         })

#     @http.route('/web_quick_count/web_quick_count/objects/<model("web_quick_count.web_quick_count"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_quick_count.object', {
#             'object': obj
#         })

