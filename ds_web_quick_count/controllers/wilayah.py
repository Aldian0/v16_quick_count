import base64
from odoo import http
from odoo.http import request

class WilayahController(http.Controller):
    # ------------------------------ WILAYAH ---------------------------------------------
    # FILTER KOTA BY PROVINSI
    @http.route('/get_kota_by_provinsi', type='json', auth='public') 
    def get_kota_by_provinsi(self, provinsi_id):
        print(provinsi_id)
        kota_records = request.env['ds.ref.kota'].sudo().search([('propinsi_id', '=', int(provinsi_id))])
        kota_data = [{'id': kota.id, 'name': kota.name} for kota in kota_records]
        return {'status': 200, 'kota': kota_data}
        
    # FILTER KECAMATAN BY KOTA
    @http.route('/get_kecamatan_by_kota', type='json', auth='public') 
    def get_kecamatan_by_kota(self, kota_id):
        kecamatan_records = request.env['ds.ref.kecamatan'].sudo().search([('kota_id', '=', int(kota_id))])
        kecamatan_data = [{'id': kecamatan.id, 'name': kecamatan.name} for kecamatan in kecamatan_records]
        return {'status': 200, 'kecamatan': kecamatan_data}

    # FILTER DESA BY KECAMATAN
    @http.route('/get_desa_by_kecamatan', type='json', auth='public') 
    def get_desa_by_kecamatan(self, kecamatan_id):
        desa_records = request.env['ds.ref.desa'].sudo().search([('kecamatan_id', '=', int(kecamatan_id))])
        desa_data = [{'id': desa.id, 'name': desa.name} for desa in desa_records]
        return {'status': 200, 'desa': desa_data}