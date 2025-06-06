
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError, Warning

class DsSaksi(models.Model):
    _name = 'ds.saksi'
    _description = 'Ds Saksi'
    _inherit     = ['mail.thread', 'mail.activity.mixin']
    _inherits       = {'res.partner' : 'partner_id'}

    @api.model
    def create(self, vals):
        vals['nomor'] = self.env['ir.sequence'].next_by_code('ds.saksi')
        rekaman = super(DsSaksi, self).create(vals)
        return rekaman


    STATE = [
        ('terdaftar', 'Terdaftar'),
        ('belum', 'Belum Terdaftar'),
    ]
    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)
    is_saksi        = fields.Boolean(default=True)
    koordinator_id  = fields.Many2one(comodel_name='ds.koordinator', string='Koordinator')
    tps_id             = fields.Many2one(comodel_name='ds.tps', string='Tps')
    hitung_cepat_ids = fields.One2many(comodel_name='ds.hitung.cepat', inverse_name='saksi_id', string='Hitung Cepat')
    state          = fields.Selection(string='Akun', selection=STATE, default='belum')

    def create_login_saksi(self):
        for item in self:
            if not item.email:
                raise UserError(_('Maaf.. Saksi %s tersebut belum memiliki alamat Email. Silakan isi dahulu' % item.name))

            if not item.partner_id.user_id:
                vals = {
                    'partner_id': item.partner_id.id,
                    'login': item.email,
                    'password': f"{item.nik}",
                    'company_id': self.env.ref('base.main_company').id,
                    'groups_id': [(6, 0, [
                                            self.env.ref('ds_base_quick_count.group_quick_count_user').id,
                                            self.env.ref('base.group_user').id
                    ])]
                }
                user_id = self.env['res.users'].create(vals)
                item.partner_id.user_id = user_id
                self.state = 'terdaftar'

    # ------------------------------- KONFIRMASI MASUKAN KE AKUN PORTAL --------------------------------
    def login_portal(self):
        portal_group = self.env.ref('base.group_portal')
        user_model = self.env['res.users']
        for rec in self:
            existing_user = user_model.search([('login', '=', rec.nik)], limit=1)
            if existing_user:
                raise ValidationError("Pengguna dengan nomor KTP %s Sudah Terdaftar.", rec.nik)
                continue

            # ------------------------ MEMBUAT USER PORTAL ------------------------
            new_user = user_model.create({
                'name': rec.name,
                'login': rec.email,
                'email': rec.email,
                'partner_id': rec.partner_id.id,
                'password': rec.nik,
                'groups_id': [(6, 0, [portal_group.id])],
            })

            # ------------------------ LOGIN USER PORTAL KIRIM EMAIL --------------------------------
            _logger.info('Created new portal user %s with email %s.', new_user.name, new_user.email)
            rec.state = 'terdaftar'

            # ------------------------ TEMPLATE EMAIL ----------------------------------------------
            mail_content = _(
                '<h3>Pendaftaran akun anda sudah dikonfirmasi oleh kami</h3><br/>Hi %s, <br/> Terimakasih, '
                'pendaftaran akun Anda telah dikonfirmasi oleh kami!<br/>'
                'Sekarang, Anda dapat melanjutkan untuk memesan persewaan armada kami secara online.<br/><br/>'
                'Silahkan Log in menggunakan akun berikut : <br/><br/>'
                '<table><tr><td>Email : %s<td/><tr/>'
                '<tr><td>Password  : No. Ktp Anda<td/><tr/>'
                '<table/>'
                '<br/>Jika Anda memiliki pertanyaan atau membutuhkan bantuan lebih lanjut,'
                '<br/>jangan ragu untuk menghubungi tim layanan kami.'
                '<br/><br/>Selamat menikmati layanan kami!'
                '<br/><br/>Admin,'
                '<br/><br/><br/>%s'
            ) % \
                       (rec.name, rec.email,self.env.user.partner_id.name)
            main_content = {
                'subject': "Pendaftaran Akun Portal",
                'author_id': self.env.user.partner_id.id,
                'body_html': mail_content,
                'email_to': rec.email,
            }
            self.env['mail.mail'].create(main_content).send()
        return True
    
    
