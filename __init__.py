# Importación diferida para evitar circularidad
from . import models
from . import controllers

def post_init_hook(cr, registry):
    from odoo import api, SUPERUSER_ID
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].set_param('bera_motos.api_key', api_key)