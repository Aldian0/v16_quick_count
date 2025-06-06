
from odoo import models, fields, api
class DsPemilihan(models.Model):
    _name           = 'ds.pemilihan'
    _description    = 'Ds Pemilihan'

    name                    = fields.Char(string='Nama')
    calon_jabatan_id        = fields.Many2one(comodel_name='ds.calon.jabatan', string='Calon Jabatan')
    paslon_ids              = fields.One2many(comodel_name='ds.paslon', inverse_name='pemilihan_id', string='Paslon')
    # partai_id               = fields.Many2one(comodel_name='ds.partai', string='Partai', related='field_name')
    gambar                  = fields.Image('gambar')

    pemilihan_ids           = fields.One2many(comodel_name='ds.hitung.cepat', inverse_name='pemilihan_id', string='Hitungan', readonly=True, copy=False)
    

    









