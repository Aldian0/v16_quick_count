# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class base_quick_count(models.Model):
#     _name = 'base_quick_count.base_quick_count'
#     _description = 'base_quick_count.base_quick_count'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

