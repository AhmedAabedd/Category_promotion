from odoo import models, fields, api, _




class PromotionWizard(models.TransientModel):
    _name = 'promotion.wizard'


    order_id = fields.Many2one('sale.order')
    promotion_id = fields.Many2one(
        'product.product',
        domain="[('is_promotion', '=', True)]",
        string="Promotions",
    )

    def action_confirm_promotion(self):
        for rec in self:
            rec.order_id.promotion_id = rec.promotion_id.id
            rec.order_id.action_add_promotion()
