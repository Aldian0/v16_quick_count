import base64
from odoo import http
from odoo.http import request

class QuickCountController(http.Controller):

    @http.route('/', auth='public', website=True)
    def home_page(self, **kw):
        # res.company request.env['res.company'].sudo().search([]), 
        # print(request.env.user.company_id.name)
        data = {
            'company_data' : request.env.user.company_id,
            'pemilihan_datas' : request.env['ds.pemilihan'].sudo().search([]),
        }
        return request.render('ds_web_quick_count.web_home_page', data)
    @http.route('/my', auth='user', website=True)
    def my_page(self, **kw):
        # res.company request.env['res.company'].sudo().search([]), 
        partner_id = request.env['res.users'].browse(request.uid).partner_id

        # print(request.env.user.company_id.name)
        data = {
            'company_data'  : request.env.user.company_id,
            'saksi_data'    : request.env['ds.saksi'].sudo().search([('partner_id', '=', partner_id.id)]),
        }
        return request.render('ds_web_quick_count.web_pengisian_page', data)
    
    @http.route('/pengisian', auth='user', website=True)
    def pengisian_page(self, **kw):
        # res.company request.env['res.company'].sudo().search([]), 
        partner_id = request.env['res.users'].browse(request.uid).partner_id

        if partner_id.is_saksi:
            # print(request.env.user.company_id.name)
            data = {
                'company_data'  : request.env.user.company_id,
                'saksi_data'    : request.env['ds.saksi'].sudo().search([('partner_id', '=', partner_id.id)]),
            }
            return request.render('ds_web_quick_count.web_pengisian_page', data)
        else:
            return request.redirect('/web')
    
    @http.route('/pengisian/<int:hitung_cepat_id>', auth='user', website=True)
    def pengisian_paslon_page(self, hitung_cepat_id, **kw):
        # res.company request.env['res.company'].sudo().search([]), 
        # print(pilihan_id)
        # print(request.env.user.company_id.name)
        data = {
            'company_data' : request.env.user.company_id,
            'hitung_cepat' : request.env['ds.hitung.cepat'].sudo().browse(int(hitung_cepat_id)),

        }
        return request.render('ds_web_quick_count.web_pengisian_page_paslon', data)
    
    @http.route('/form_plano_save/<int:hitung_cepat_id>', auth='user', website=True, csrf=False, methods=['POST'])
    def form_save_plano_page(self, hitung_cepat_id, **kw):
        # plano = create({})
        nama = kw.get('nama')
        keterangan = kw.get('keterangan')
        image = request.httprequest.files.get('gambar')
        image_base64 = base64.b64encode(image.read()) if image else False
        request.env['ds.chasil.plano'].sudo().create({
            'name'                  : nama,
            'upload_chasil_plano'   : image_base64,
            'keterangan'            : keterangan,
            'hitung_cepat_id'       : int(hitung_cepat_id)
        })
        return request.redirect('/pengisian/{}'.format(int(hitung_cepat_id)))
    @http.route('/delete_plano/<int:hitung_cepat_id>/<int:plano_id>', auth='user', website=True)
    def delete_plano_page(self, hitung_cepat_id,plano_id, **kw):
        request.env['ds.chasil.plano'].sudo().browse(int(plano_id)).unlink()
        return request.redirect('/pengisian/{}'.format(int(hitung_cepat_id)))
    
    @http.route('/form_suara_input/<int:hitung_cepat_id>/<int:suara_paslon_id>', auth='user', website=True, csrf=False, methods=['POST'])
    def form_save_suara_page(self, hitung_cepat_id, suara_paslon_id, **kw):
        # suara = create({})
        suara = kw.get('suara')
        print(suara)

        line_hitung_cepat_id = request.env['ds.line.hitung.cepat'].sudo().browse(int(suara_paslon_id))
        line_hitung_cepat_id.write({
            'jumlah_suara' : suara
        })
        return request.redirect('/pengisian/{}'.format(int(hitung_cepat_id)))
    @http.route('/form_konfirmasi/<int:hitung_cepat_id>', auth='user', website=True, csrf=False, methods=['POST'])
    def form_konfirmasi_page(self, hitung_cepat_id, **kw):

        hitung_cepat_id = request.env['ds.hitung.cepat'].sudo().browse(int(hitung_cepat_id))

        jml_pemilih_hadir   = kw.get('jml_pemilih_hadir')
        jml_dpt             = kw.get('jml_dpt')
        jml_suara_sah       = kw.get('jml_suara_sah')
        jml_suara_tidak_sah = kw.get('jml_suara_tidak_sah')
        # print('jml_pemilih_hadir',jml_pemilih_hadir,'\njml_dpt',jml_dpt,'\njml_suara_sah',jml_suara_sah,'\njml_suara_tidak_sah',jml_suara_tidak_sah)
        hitung_cepat_id.write({
            'jml_pemilih_hadir': jml_pemilih_hadir,
            'jml_dpt': jml_dpt,
            'jml_suara_sah': jml_suara_sah,
            'jml_suara_tidak_sah': jml_suara_tidak_sah,
            # 'state': 'done'
        })
        return request.redirect('/pengisian/{}'.format(int(hitung_cepat_id)))
