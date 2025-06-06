from odoo import models, fields, api



class DsPartai(models.Model):
    _name           = 'ds.partai'
    _description    = 'Ds Partai'
    _inherit        = ['mail.thread', 'mail.activity.mixin']

    name            = fields.Char(string='Nama Partai', required=True)
    logo_partai     = fields.Image('Logo Partai', max_width=200, max_height=200)

    
