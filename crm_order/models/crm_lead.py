# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Lead(models.Model):
    _inherit = 'crm.lead'

    x_lead_category = fields.Selection(
        selection=[
            ('residential', 'Residential'),
            ('business', 'Business'),
            ('governmental', 'Governmental')
        ],
        string="X Lead Category",
        tracking=True
    )

    x_delivery_deadline = fields.Date(
        string='x Delivery Deadline',
        tracking=True
    )

    x_approved_by = fields.Many2one(
        string='x Approved By',
        comodel_name='res.users',
        tracking=True
    )

    x_approved_date = fields.Date(
        string='x Approved Adate',
        default=fields.Date.context_today, tracking=True
    )

    x_installation_required = fields.Boolean(
        string='x Installation Required',
        tracking=True
    )

    x_installation_date = fields.Date(
        string='x Installation Date',
        tracking=True
    )

    x_contract_reference = fields.Char(
        string='x contract reference',
        tracking=True
    )

    x_support_required = fields.Boolean(
        string='x Support Required',
        tracking=True
    )

    @api.depends('x_approved_date')
    def _compute_duration_since_approved(self):
        for record in self:
            if record.x_approved_date:
                record.x_duration_since_approved = (
                    fields.Date.context_today(
                        record) - record.x_approved_date).days

    x_duration_since_approved = fields.Integer(
        string="x Duration since approved",
        compute='_compute_duration_since_approved',
        store=True
    )

    def action_approve_order(self):
        self.ensure_one()
        self.write({
            'x_delivery_deadline': fields.Date.context_today(self),
            'x_approved_by': self.env.user.id
        })
