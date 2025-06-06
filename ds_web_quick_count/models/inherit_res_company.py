
from odoo import models, fields, api

class ResCompany(models.Model):
    
    _inherit = 'res.company'
    
    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------
    
    website_profile_image = fields.Binary(
        string='Profile Website',
        attachment=True
    )

    title = fields.Char(string='Title')
    company_deskription = fields.Text(string='Deskripsi')
    


    