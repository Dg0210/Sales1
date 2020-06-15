from odoo import models,fields


class Customer(models.Model):
    _inherit = "res.partner"
    cmt = fields.Char("CMT")
