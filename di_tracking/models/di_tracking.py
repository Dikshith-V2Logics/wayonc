# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date, timedelta,datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class DiTracking(models.Model):
    _name = 'di.tracking'
    _description = "DI Tracking"
    _order = "name desc"
    _inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Many2one('res.partner',string="Investor Name")
    
