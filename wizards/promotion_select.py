from odoo import models, fields, api, _




class PromotionSelect(models.TransientModel):
    _name = 'promotion.select'



    promotion_id = fields.Many2one(
        'product.product',
        domain="[('is_promotion', '=', True)]",
        string="Promotion Name",
        required=True
    )