# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"


    pan_no = fields.Char(string="Pan No.")
    emp_id = fields.Char(string="Employee id",required=True, copy=False, readonly=True, default=lambda self: _('New'))


    @api.model
    def create(self, vals):
        if vals.get('emp_id', _('New')) == _('New'):
            vals['emp_id'] = self.env['ir.sequence'].next_by_code('hr.employee') or _('New')
        result = super(HrEmployee, self).create(vals)
        return result
