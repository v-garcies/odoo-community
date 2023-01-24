# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.tools.translate import html_translate

class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    website_description_bottom = fields.Html('Bottom category description', sanitize_attributes=False, translate=html_translate, sanitize_form=False)
