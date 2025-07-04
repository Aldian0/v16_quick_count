from odoo import models, fields, api, _

# omod 

class RefPropinsi(models.Model):
    _name           = 'ds.ref.propinsi'
    _description    = 'Ref Propinsi'

    # ofchar 
    name            = fields.Char(string='Nama', required=True)
    kode            = fields.Char(string='Kode')
    singkat         = fields.Char(string='Singkatan')
    keterangan      = fields.Text(string='Keterangan')


    kota_ids        = fields.One2many(comodel_name='ds.ref.kota', inverse_name='propinsi_id', string='Kota/Kabupaten')
    
class RefKota(models.Model):
    _name           = 'ds.ref.kota'
    _description    = 'Ref Kota'


    name            = fields.Char(string='Nama Kota', required=True)
    kode            = fields.Char(string='Kode Kota')
    singkat         = fields.Char(string='Singkatan')
    keterangan      = fields.Text(string='Keterangan')


    propinsi_id     = fields.Many2one(comodel_name='ds.ref.propinsi', string='Propinsi')
    kecamatan_ids   = fields.One2many(comodel_name='ds.ref.kecamatan', inverse_name='kota_id', string='Kecamatan')
    

    
class RefKecamatan(models.Model):
    _name           = 'ds.ref.kecamatan'
    _description    = 'Ref Kecamatan'

    name            = fields.Char(string='Nama Kecamatan', required=True)
    kode            = fields.Char(string='Kode Kecamatan')
    singkat         = fields.Char(string='Singkatan')
    keterangan      = fields.Text(string='Keterangan')

    kota_id         = fields.Many2one(comodel_name='ds.ref.kota', string='Kota')
    desa_ids        = fields.One2many(comodel_name='ds.ref.desa', inverse_name='kecamatan_id', string='Desa/Kelurahan')
    


class RefDesa(models.Model):
    _name           = 'ds.ref.desa'
    _description    = 'Ref Desa'

    name            = fields.Char(string='Desa/Kelurahan', required=True)
    kode            = fields.Char(string='Kode Desa/Kelurahan')
    keterangan      = fields.Text(string='Keterangan')

    kecamatan_id    = fields.Many2one(comodel_name='ds.ref.kecamatan', string='Kecamatan')
    
    



    
    