from odoo import models, fields, api




class DsCalon(models.Model):
    _name = 'ds.calon'
    _description = 'Ds Calon'

    _inherit     = ['mail.thread', 'mail.activity.mixin']
    _inherits    = {'res.partner' : 'partner_id'}

    partner_id   = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)

    partai_id    = fields.Many2one(comodel_name='ds.partai', string='Partai')

    # paslon_id    = fields.Many2one(comodel_name='ds.paslon', string='Paslon')
    paslon_id = fields.Many2one(comodel_name='ds.paslon', string='Paslon')
    is_calon        = fields.Boolean(default=True)
