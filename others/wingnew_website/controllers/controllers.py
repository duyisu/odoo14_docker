# -*- coding: utf-8 -*-
# from odoo import http


# class WingnewWebsite(http.Controller):
#     @http.route('/wingnew_website/wingnew_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wingnew_website/wingnew_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wingnew_website.listing', {
#             'root': '/wingnew_website/wingnew_website',
#             'objects': http.request.env['wingnew_website.wingnew_website'].search([]),
#         })

#     @http.route('/wingnew_website/wingnew_website/objects/<model("wingnew_website.wingnew_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wingnew_website.object', {
#             'object': obj
#         })
