# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError


class ResClient(models.Model):
    _name = 'res.client'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin', 'utm.mixin']

    name = fields.Char(string="Client Id",required=True, copy=False, readonly=True, default=lambda self: _('New'))

    client_name = fields.Char(string="Name")
    last_name = fields.Char(string="Last name")

    partner_ref_id = fields.Many2one('res.partner',string="Contact Ref Id")

    company_id = fields.Many2one('res.company', string='Company', index=True, default=lambda self: self.env.company.id)
    user_id = fields.Many2one('res.users', copy=False, tracking=True,
        string='User',default=lambda self: self.env.user,required=True)
    active = fields.Boolean("Active", default=True, help="If the active field is set to false, it will allow you to hide the case without removing it.")
    returns_percent = fields.Float(string="% of Returns")
    # investment_line_ids = fields.One2many('investment.details','client_id',string="Investment details")


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('res.client') or _('New')
        res = super(ResClient, self).create(vals)
        return res




# class InvestmentDetails(models.Model):
#     _name = 'investment.details'

#     # whatever the payment done by client will be added in line based on periods
#     name = fields.Char(string="Investment Sequence")
#     client_id = fields.Many2one('res.client')

#     amount_invested = fields.Float(string="Amount Invested")
#     processing_charges = fields.Float(string="Processing Charges")
#     date_of_investment = fields.Date(string="Date of Investment")
#     date_of_expiry = fields.Date(string="Date of Expiry") #it should be automatically fetched
#     returns_percent = fields.Float(string="% of Returns",related="client_id.returns_percent")

#     @api.onchange('amount_invested')
#     def _fetch_processing_charges(self):
#         charges_id = self.env['processing.charges.rule'].search([('min_value','>=',self.amount_invested),('max_value','<=',self.amount_invested)])
#         if charges_id:
#             for line in charges_id:
#                 self.processing_charges = line.id
#         else:
#             raise ValidationError(_("Charges not defined for the set amount. Kindly change amount and retry..!"))
