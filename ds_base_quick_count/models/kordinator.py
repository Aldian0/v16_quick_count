from odoo import models, fields, api, _

from odoo.exceptions import UserError, Warning


class DsKoordinator(models.Model):
    _name = 'ds.koordinator'
    _description = 'Ds Koordinator'
    _inherit     = ['mail.thread', 'mail.activity.mixin']
    _inherits       = {'res.partner' : 'partner_id'}

    @api.model
    def create(self, vals):
        vals['nomor'] = self.env['ir.sequence'].next_by_code('ds.koordinator')
        rekaman = super(DsKoordinator, self).create(vals)
        return rekaman

    is_kordinator_lapangan = fields.Boolean(default=True)

    STATE = [
        ('terdaftar', 'Terdaftar'),
        ('belum', 'Belum Terdaftar'),
    ]

    partner_id      = fields.Many2one(comodel_name='res.partner', string='Partner ID',ondelete='cascade', required=True)
    saksi_ids        = fields.One2many(comodel_name='ds.saksi', inverse_name='koordinator_id', string='Saksi')
    state          = fields.Selection(string='Akun', selection=STATE, default='belum')
    

    def create_login_kordes(self):
        for item in self:
            if not item.email:
                raise UserError(_('Maaf.. Kordes %s tersebut belum memiliki alamat Email. Silakan isi dahulu' % item.name))

            if not item.partner_id.user_id:
                vals = {
                    'partner_id': item.partner_id.id,
                    'login': item.email,
                    'password': item.nik,
                    'company_id': self.env.ref('base.main_company').id,
                    'groups_id': [(6, 0, [
                                            self.env.ref('ds_base_quick_count.group_quick_count_user').id,
                                            self.env.ref('base.group_user').id
                    ])]
                }
                user_id = self.env['res.users'].create(vals)
                item.partner_id.user_id = user_id
                self.state = 'terdaftar'

