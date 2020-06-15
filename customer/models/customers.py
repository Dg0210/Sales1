from odoo import models, fields


class Customer(models.Model):
    _inherit = "res.partner"
    cmt = fields.Char("So Chung Minh Thu")
    _sql_constraints = [('cmt','UNIQUE (cmt)','Course all already exists'), ]
