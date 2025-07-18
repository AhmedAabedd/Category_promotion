from odoo import models, fields, api, _



class PromotionProduct(models.Model):
    _inherit = 'product.product'


    is_promotion = fields.Boolean(string="Is Promotion", required=True)
    discount_percentage = fields.Float(string="Discount (%)", required=True)
    min_quantity = fields.Float(string="Min Quantity")

    promo_on = fields.Selection([
        ('cheapest', 'Cheapest'),
        ('expensive', 'More Expensive'),
    ], default='cheapest')
    