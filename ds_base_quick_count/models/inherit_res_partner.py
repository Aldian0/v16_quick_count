from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit        = 'res.partner'

    is_saksi                = fields.Boolean(string='Saksi')
    is_kordinator_lapangan  = fields.Boolean(string='Kordinator Lapangan')
    is_calon                = fields.Boolean(string='Paslon')


    AGAMA = [
        ('islam','Islam'),
        ('kristen','Kristen'),
        ('katolik','Katolik'),
        ('hindu','Hindu'),
        ('budha','Budha'),
        ('konghucu','Kong Hu Chu'),
        ('lainnya','Lainnya'),
    ]

    JENIS_KELAMIN = [
        ('l','Laki-laki'),
        ('p','Perempuan'),
    ]

    nomor           = fields.Char(string='Nomor', default='AUTO')
    is_terkirim     = fields.Selection(string='Kirim', selection=[('sudah', 'Sudah Mengirim'), ('belum', 'Belum Mengirim')], default='belum')
    propinsi_id     = fields.Many2one(comodel_name='ds.ref.propinsi', string='Propinsi')
    kota_id         = fields.Many2one(comodel_name='ds.ref.kota', string='Kota/Kabupaten')
    kecamatan_id    = fields.Many2one(comodel_name='ds.ref.kecamatan', string='Kecamatan')
    desa_id         = fields.Many2one(comodel_name='ds.ref.desa', string='Desa/Kelurahan')
    nik             = fields.Char(string='NIK')
    agama           = fields.Selection(selection=AGAMA,  string="Agama",  help="")
    jenis_kel       = fields.Selection(string='Jenis Kelamin', selection=JENIS_KELAMIN)






