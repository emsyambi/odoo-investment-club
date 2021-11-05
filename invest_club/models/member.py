from odoo import api, fields, models, _


class InvestmentClubMember(models.Model):
    _name = "investment.club.member"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Investment Club Member"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'),
                              ('cancel', 'Cancelled')], default="draft", string="Status", tracking=True)
    acpartner_id = fields.Many2one('res.partner', string='Accountability Partner')
    image = fields.Binary(string='Patient Image')
