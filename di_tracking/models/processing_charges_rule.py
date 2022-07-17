# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date, timedelta,datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class ProcessingChargesRule(models.Model):
	_name = 'processing.charges.rule'
	_description = 'Processing Charges'
	_inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

	name = fields.Char(string="Price")
	min_value = fields.Float(string='Minimum threshold')
	max_value = fields.Float(string='Maximum threshold')
	company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)
	user_id = fields.Many2one('res.users', copy=False, tracking=True,
		string='User',default=lambda self: self.env.user,required=True)
	active = fields.Boolean("Active", default=True, help="If the active field is set to false, it will allow you to hide the case without removing it.")
