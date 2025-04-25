from odoo import http, SUPERUSER_ID
from odoo.http import request, Response
import json

class BeraMotosApiController(http.Controller):

    @http.route('/api/v1/motos/facturas', type='http', auth='none', methods=['GET'], csrf=False)
    def get_facturas_motos(self, **kw):
        try:
            # Autenticación
            if not self._check_api_key():
                return self._error_response("Acceso no autorizado", 401)
            
            # Consulta usando SUPERUSER_ID
            env = request.env(user=SUPERUSER_ID)
            # Filtros base
            domain = [
                ('is_factura_de_moto', '=', True),    # Es factura de moto
                ('move_type', '=', 'out_invoice'),     # Es factura de cliente
                ('state', '=', kw.get('estado', 'posted')),  # Estado publicado por defecto
                ('branch_id.name', '=', 'PLANTA LA MORITA')  # Solo facturas de PLANTA LA MORITA
            ]
            
            # Búsqueda limitada a las últimas 10 facturas (activa por defecto)
            facturas = env['account.move'].search(domain, limit=10, order='create_date desc')
            
            # Búsqueda de todas las facturas (comentada)
            # facturas = env['account.move'].search(domain, order='create_date desc')
            
            # Formateo de respuesta
            data = {
                'facturas': [
                    {
                        'numero': f.name,
                        'fecha': f.invoice_date.strftime('%Y-%m-%d') if f.invoice_date else None,
                        'cliente': f.partner_id.name,
                        'items': [
                            {
                                'producto': line.product_id.name,
                                'cantidad': line.quantity,
                                'precio': line.price_unit,
                                'total': line.price_total
                            }
                            for line in f.invoice_line_ids
                        ]
                    }
                    for f in facturas
                ]
            }
            
            return Response(
                json.dumps(data, ensure_ascii=False, indent=4),  # indent=4 para formatear el JSON
                status=200,
                content_type='application/json; charset=utf-8'
            )
            
        except Exception as e:
            return self._error_response(str(e), 500)

    def _check_api_key(self):
        api_key = request.env['ir.config_parameter'].sudo().get_param('bera_motos.api_key')
        provided_key = request.httprequest.headers.get('Authorization', '').replace('Bearer ', '')
        return api_key and api_key == provided_key

    def _error_response(self, message, code):
        return Response(
            json.dumps({'error': message}),
            status=code,
            content_type='application/json'
        )