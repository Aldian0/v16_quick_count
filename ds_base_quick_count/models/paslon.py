from odoo import models, fields, api




class DsPaslon(models.Model):
    _name               = 'ds.paslon'
    _description        = 'Ds Paslon'

    name                = fields.Char(string='Nama', readonly=False, copy=False)
    gambar_paslon       = fields.Image('Gambar Paslon')
    calon_jabatan_id    = fields.Many2one(comodel_name='ds.calon.jabatan', string='Calon Jabatan')
    partai_id           = fields.Many2one(comodel_name='ds.partai', string='Partai')
    partai_ids          = fields.Many2many(comodel_name='ds.partai', string='Partai Pengusung')
    calon_ids           = fields.One2many(comodel_name='ds.calon', inverse_name='paslon_id', string='Calon Pejabat')
    nama_calon          = fields.Char(compute='compute_nama_paslon', string='Nama Calon', store=True)
    
    @api.depends('calon_ids', 'calon_ids.name')
    def compute_nama_paslon(self):
        for rec in self:
            nama_calon = ''
            for calon in rec.calon_ids:
                nama_calon += calon.name + ' - '
            rec.nama_calon = nama_calon.rstrip(' - ')
    
    pemilihan_id        = fields.Many2one(comodel_name='ds.pemilihan', string='Pemilihan')
    hasil_ids           = fields.One2many(comodel_name='ds.line.hitung.cepat', inverse_name='paslon_id', string='Hasil', readonly=True, copy=False)
    hasil                = fields.Integer(string='Jumlah Suara Terhitung', compute='_compute_suara', store=True)
    presentase          = fields.Float(string='Presentase', compute='_compute_presentase', store=True)

    @api.depends('hasil_ids', 'hasil_ids.state', 'hasil')
    def _compute_presentase(self):
        for rec in self:
            # Ensure calon_jabatan_id is present before searching
            if rec.calon_jabatan_id:
                # Find all related 'ds.line.hitung.cepat' records
                obj_hitung_cepat = rec.env['ds.line.hitung.cepat'].sudo().search(
                    [('calon_jabatan_id', '=', rec.calon_jabatan_id.id)]
                )
                
                # Sum the 'jumlah_suara' from the found records
                all_hasil = sum(obj_hitung_cepat.mapped('jumlah_suara'))
                
                # Avoid division by zero
                if all_hasil > 0:
                    rec.presentase = rec.hasil / all_hasil * 100
                else:
                    rec.presentase = 0.0
            else:
                rec.presentase = 0.0


    @api.depends('hasil_ids','hasil_ids.state')
    def _compute_suara(self):
        for rec in self:
            obj_hitung_cepat    = rec.env['ds.line.hitung.cepat'].sudo().search(
                [('paslon_id', '=', rec.id),
                 ('state', '=', 'done')]
                 )
            rec.hasil           = sum(obj_hitung_cepat.mapped('jumlah_suara'))
                
class DsCalonJabatan(models.Model):
    _name           = 'ds.calon.jabatan'
    _description    = 'Ds Calon Jabatan'

    name            = fields.Char(string='Nama')
    
