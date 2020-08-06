# Author: Abdelrahman Helaly
# Contact: < AH3laly@gmail.com , https://Github.com/AH3laly >
# Project: Odoo 10 Customer Service. 
# Description: Odoo 10 Customer Service Module.
# License: Science not for Monopoly.

# -*- coding: utf-8 -*-
from odoo import http


@http.route('/cs/customers_list/', auth='public')
def customers_list(self, **kw):
    return "Customers List Here"


    

# class Cs(http.Controller):
#     @http.route('/cs/cs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cs/cs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cs.listing', {
#             'root': '/cs/cs',
#             'objects': http.request.env['cs.cs'].search([]),
#         })

#     @http.route('/cs/cs/objects/<model("cs.cs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cs.object', {
#             'object': obj
#         })
