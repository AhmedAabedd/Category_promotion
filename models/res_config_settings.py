from odoo import models, fields, api, _




class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'





    category_promotion_active = fields.Boolean(
        string="Category Promotions",
        help="Activate or deactivate the category promotions system",
        config_parameter='category_promotion.enable_promotions'
    )