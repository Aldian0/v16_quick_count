from odoo import models, fields, api, _

class DsTps(models.Model):
    _name           =  'ds.tps'
    _description    =  'Ds Tps'
    _inherit     = ['mail.thread', 'mail.activity.mixin']

    name            = fields.Char(string='Nama TPS')

    nomor_tps       = fields.Char(string='Nomor TPS')

    
    propinsi_id     = fields.Many2one(comodel_name='ds.ref.propinsi', string='Propinsi')
    kota_id         = fields.Many2one(comodel_name='ds.ref.kota', string='Kota/Kabupaten')
    kecamatan_id    = fields.Many2one(comodel_name='ds.ref.kecamatan', string='Kecamatan')
    desa_id         = fields.Many2one(comodel_name='ds.ref.desa', string='Desa/Kelurahan')

    alamat          = fields.Text(string='Alamat')

    
