from odoo import models, fields, api



class DsHitungCepat(models.Model):
    _name = 'ds.hitung.cepat'
    _description = 'Ds Hitung Cepat'
    _inherit     = ['mail.thread', 'mail.activity.mixin']

    READONLY_STATES         = {'proses': [('readonly', True)], 'done': [('readonly', True)]}
    STATE = [
        ('draft', 'Draft'),
        ('proses', 'Proses'),
        ('done', 'Done'),
    ]
    state                   = fields.Selection(string='Status', selection=STATE, default='draft', required=True, copy=False)

    name                    = fields.Char(string='Nama', states=READONLY_STATES, tracking=True)
    saksi_id                = fields.Many2one(comodel_name='ds.saksi', string='Saksi', states=READONLY_STATES, tracking=True)
    koordinator_id          = fields.Many2one(comodel_name='ds.koordinator', string='Koordinator', related='saksi_id.koordinator_id', store=True, states=READONLY_STATES, tracking=True)
    tps_id                  = fields.Many2one(comodel_name='ds.tps', string='Tps', related='saksi_id.tps_id', store=True, states=READONLY_STATES, tracking=True)
    
    propinsi_id             = fields.Many2one(comodel_name='ds.ref.propinsi', string='Propinsi TPS', related='tps_id.propinsi_id', store=True)
    kota_id                 = fields.Many2one(comodel_name='ds.ref.kota', string='Kota/Kabupaten TPS', related='tps_id.kota_id', store=True)
    kecamatan_id            = fields.Many2one(comodel_name='ds.ref.kecamatan', string='Kecamatan TPS', related='tps_id.kecamatan_id', store=True)
    desa_id                 = fields.Many2one(comodel_name='ds.ref.desa', string='Desa/Kelurahan TPS', related='tps_id.desa_id', store=True)
    alamat                  = fields.Text(string='Alamat TPS', related='tps_id.alamat', store=True)
    
    calon_jabatan_id        = fields.Many2one(comodel_name='ds.calon.jabatan', string='Calon Jabatan', states=READONLY_STATES, tracking=True)
    pemilihan_id            = fields.Many2one(comodel_name='ds.pemilihan', string='Pemilihan', states=READONLY_STATES, tracking=True)
    is_terisi               = fields.Boolean(string='Terisi', default=False, states=READONLY_STATES, tracking=True)
    is_tersimpan            = fields.Boolean(string='Tersimpan', default=False, states=READONLY_STATES, tracking=True)
    
    jml_pemilih_hadir       = fields.Integer(string="Jumlah Pemilih Hadir")
    jml_dpt                 = fields.Integer(string="Jumlah DPT")

    jml_suara_sah           = fields.Integer(string="Jumlah Suara Sah")
    jml_suara_tidak_sah     = fields.Integer(string="Jumlah Suara Tidak Sah")



    golput                  = fields.Integer(string="Golput", compute='_compute_golput', store=True)
    presentase_kehadiran    = fields.Float(string="Presentase Kehadiran", compute='_compute_presentase_kehadiran', store=True)


    peringatan              = fields.Selection(string='Peringatan',
                                               selection=[('tidak_nomal', 'Tidak Normal'),
                                                          ('normal', 'Normal'),
                                                          ('belum_terdeteksi', 'Belum Terdeteksi')], compute='_compute_peringatan', store=True)
    keterangan              = fields.Text(string='Keterangan',  compute='_compute_peringatan')

    @api.depends('line_hitung_cepat_ids','jml_dpt',  'jml_suara_sah', 'jml_suara_tidak_sah', 'jml_pemilih_hadir','state')
    def _compute_peringatan(self):
        for record in self:
            keterangan = ""
            nilai = 0
            if record.jml_suara_sah and record.line_hitung_cepat_ids:
                data_pilihan = record.line_hitung_cepat_ids
                total_suara_sah = sum(data_pilihan.mapped('jumlah_suara'))
                if record.jml_suara_sah != total_suara_sah:
                    record.peringatan = 'tidak_nomal'
                    keterangan += f"Jumlah Suara Sah {record.jml_suara_sah} Tidak Sama dengan Total Suara Perolehan {total_suara_sah} \n"
                    nilai +=1
                record.jml_dpt
                jumlah_pemilih = (record.jml_suara_sah + record.jml_suara_tidak_sah)
                if record.jml_pemilih_hadir != jumlah_pemilih:
                    keterangan += f"Jumlah Pemilih Hadir {record.jml_pemilih_hadir} Tidak Sama dengan Jumlah Pemilih Perolehan {jumlah_pemilih} \n"
                    nilai +=1
                if record.jml_dpt < record.jml_pemilih_hadir:
                    keterangan += f"Jumlah DPT {record.jml_dpt} Lebih Kecil dari Jumlah Pemilih yang Hadir {record.jml_pemilih_hadir} \n"
                    nilai +=1
                if nilai > 0:
                    record.peringatan = 'tidak_nomal'
                else:
                    record.peringatan = 'normal'

            record.keterangan = keterangan
                    

    
    


    @api.depends('jml_dpt', 'jml_pemilih_hadir','state')
    def _compute_presentase_kehadiran(self):
        for record in self:
            if record.jml_dpt and record.jml_pemilih_hadir:
                record.presentase_kehadiran = (record.jml_pemilih_hadir / record.jml_dpt) * 100
            else:
                record.presentase_kehadiran = 0


    # field_name = fields.Char(compute='_compute_field_name', string='field_name')
    
    @api.depends('jml_dpt', 'jml_suara_sah', 'jml_suara_tidak_sah','state')
    def _compute_golput(self):
        for record in self:
            if record.jml_dpt and record.jml_suara_sah and record.jml_suara_tidak_sah:
                record.golput = record.jml_dpt - (record.jml_suara_sah + record.jml_suara_tidak_sah)
            else:
                record.golput = 0
        



    line_hitung_cepat_ids   = fields.One2many(comodel_name='ds.line.hitung.cepat', inverse_name='hitung_cepat_id', string='Line Hitung Cepat')
    data_chasil_plano_ids   = fields.One2many(comodel_name='ds.chasil.plano', inverse_name='hitung_cepat_id', string='Upload Chasil Plano')
    
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('ds.perhitungan')
        vals['is_tersimpan'] = True
        vals['state'] = 'proses'
        rekaman = super(DsHitungCepat, self).create(vals)
        return rekaman

    @api.onchange('pemilihan_id')
    def _onchange_pemilihan_id(self):
        # if self.pemilihan_id:
        # Jika ada record di line_hitung_cepat_ids, hapus terlebih dahulu yang terkait dengan hitung_cepat_id dan pemilihan_id
        hitung = len(self.line_hitung_cepat_ids)
        # print(hitung)
        paslon_ids = self.pemilihan_id.paslon_ids
        self.env['ds.line.hitung.cepat'].sudo().search([('hitung_cepat_id', '=', False)]).unlink()
        
        # if self.is_tersimpan :
        if hitung == 0: 
            self.is_terisi = True
        else:
            self.is_terisi = False

        if self.is_terisi == True:
            self.line_hitung_cepat_ids = False
            # self.env['ds.line.hitung.cepat'].sudo().search([('hitung_cepat_id', '=', self.id)]).unlink()
            for paslon in paslon_ids:
                # Buat baris baru di ds.line.hitung.cepat untuk setiap paslon_id
                self.env['ds.line.hitung.cepat'].create({
                    'paslon_id': paslon.id,  # id paslon
                    'hitung_cepat_id': self.id,  # id hitung cepat yang sedang diproses
                    'pemilihan_id': self.pemilihan_id.id  # id pemilihan
                })
        else :
            for paslon in paslon_ids:
                # Buat baris baru di ds.line.hitung.cepat untuk setiap paslon_id
                self.env['ds.line.hitung.cepat'].create({
                    'paslon_id': paslon.id,  # id paslon
                    'hitung_cepat_id': self.id,  # id hitung cepat yang sedang diproses
                    'pemilihan_id': self.pemilihan_id.id  # id pemilihan
                })

    def action_confirm(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'

    def action_progress(self):
        self.state = 'proses'
        


class DsChasilPlano(models.Model):
    _name = 'ds.chasil.plano'
    _description = 'Ds Chasil Plano'

    hitung_cepat_id = fields.Many2one(comodel_name='ds.hitung.cepat', string='Hitung Cepat')
    
    name                = fields.Char(string='Nama')
    upload_chasil_plano = fields.Binary(string='Gambar')
    keterangan          = fields.Text(string='Keterangan')

class DsLineHitungCepat(models.Model):
    _name = 'ds.line.hitung.cepat'
    _description = 'Hitung Cepat Line'

    hitung_cepat_id     = fields.Many2one(comodel_name='ds.hitung.cepat', string='Hitung Cepat')
    pemilihan_id        = fields.Many2one(comodel_name='ds.pemilihan', string='Pemilihan')
    paslon_id           = fields.Many2one(comodel_name='ds.paslon', string='Paslon')
    
    state               = fields.Selection(related='hitung_cepat_id.state', store=True)
    name                = fields.Char(string='Nama', related='paslon_id.name', store=True)
    gambar_paslon       = fields.Image('Gambar Paslon', related='paslon_id.gambar_paslon', store=True)
    nama_calon          = fields.Char(string='Nama Calon', store=True, related='paslon_id.nama_calon')
    calon_jabatan_id    = fields.Many2one(comodel_name='ds.calon.jabatan', string='Calon Jabatan', related='paslon_id.calon_jabatan_id', store=True)
    partai_id           = fields.Many2one(comodel_name='ds.partai', string='Partai', related='paslon_id.partai_id', store=True)

    saksi_id            = fields.Many2one(comodel_name='ds.saksi', string='Saksi', related='hitung_cepat_id.saksi_id', store=True)
    tps_id              = fields.Many2one(comodel_name='ds.tps', string='Tps', related='hitung_cepat_id.tps_id', store=True)
    jumlah_suara        = fields.Integer(string='Jumlah Suara')

    propinsi_id         = fields.Many2one(comodel_name='ds.ref.propinsi', string='Propinsi TPS', related='tps_id.propinsi_id', store=True)
    kota_id             = fields.Many2one(comodel_name='ds.ref.kota', string='Kota/Kabupaten TPS', related='tps_id.kota_id', store=True)
    kecamatan_id        = fields.Many2one(comodel_name='ds.ref.kecamatan', string='Kecamatan TPS', related='tps_id.kecamatan_id', store=True)
    desa_id             = fields.Many2one(comodel_name='ds.ref.desa', string='Desa/Kelurahan TPS', related='tps_id.desa_id', store=True)
    alamat              = fields.Text(string='Alamat TPS', related='tps_id.alamat', store=True)




