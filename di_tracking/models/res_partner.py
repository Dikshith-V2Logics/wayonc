# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_investor = fields.Boolean(string="Is Investor?")
    investment_app_created = fields.Boolean(string="Record Created",default=False)

    res_client_count = fields.Integer(string='Investor', compute='_investor_count')

    def _investor_count(self):
        for line in self:
            investor_count = self.env['res.client'].search([('partner_ref_id', '=', line.id)])
            line.res_client_count = len(investor_count)

    def action_create_investor(self):
        for line in self:
            line.investment_app_created = True
        print("--")
    
