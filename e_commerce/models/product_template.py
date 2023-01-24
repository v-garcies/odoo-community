# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.tools.translate import html_translate

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_description_top = fields.Html('Top description for the website', sanitize_attributes=False, translate=html_translate, sanitize_form=False)
