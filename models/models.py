# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cod_statv1(models.Model):
#     _name = 'cod_statv1.cod_statv1'
#     _description = 'cod_statv1.cod_statv1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
