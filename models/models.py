# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Plants(models.Model):
    _name = "nursery.plant"

    name = fields.Char("Plant name")
    price = fields.Float()


class Customer(models.Model):
    _name = "nursery.customer"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char(help="to receive news")
