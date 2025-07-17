from odoo import models, fields, api, _




class SaleOrder(models.Model):
    _inherit = 'sale.order'


    promotion_id = fields.Many2one(
        'product.product',
        domain="[('is_promotion', '=', True)]",
        string="Promotion Name",
        required=True
    )
    can_apply_promotion = fields.Boolean(compute="_compute_can_apply_promotion", store=True)

    @api.depends('order_line', 'promotion_id')
    def _compute_can_apply_promotion(self):
        for order in self:
            # Step 1: Group lines by category
            lines_by_category = {}
            for line in order.order_line:
                category = line.product_template_id.categ_id.id
                if not category:
                    continue
                if category not in lines_by_category:
                    lines_by_category[category] = self.env['sale.order.line']
                lines_by_category[category] += line

            #step 2: Loop through grouped lines and apply logic once per category
            for category_id, lines in lines_by_category.items():
                total_qty = sum(lines.mapped('product_uom_qty'))
                if total_qty >= order.promotion_id.min_quantity:
                    order.can_apply_promotion = True
                else:
                    order.can_apply_promotion = False
        print("//////////////////////// VALUE :",order.can_apply_promotion, '/////////////////////')






    def action_add_promotion(self):
        for order in self:

            # Step 1: Group lines by category
            lines_by_category = {}
            for line in order.order_line:
                category = line.product_template_id.categ_id.id
                if not category:
                    continue
                if category not in lines_by_category:
                    lines_by_category[category] = self.env['sale.order.line']
                lines_by_category[category] += line
        

            #step 2: Loop through grouped lines and apply logic once per category
            for category_id, lines in lines_by_category.items():
                total_qty = 0
                total_price = 0
                for order_line in lines:
                    total_qty += order_line.product_uom_qty
                    total_price += order_line.price_subtotal
                    if total_qty >= order.promotion_id.min_quantity:
                        discount_amount = (order.promotion_id.discount_percentage * total_price) / 100
                        category = self.env['product.category'].browse(category_id)
                        
                        # Create promotion line
                        self.env['sale.order.line'].create({
                            'order_id': order.id,
                            'product_id': order.promotion_id.id,
                            'name': f"Promotion on {category.name} ({order.promotion_id.discount_percentage}% discount)",
                            'price_unit': -discount_amount,
                            'product_uom_qty': 1,
                            'product_uom': order.promotion_id.uom_id.id,
                            'tax_id': False,
                            #'is_promotion_line': True,  # Add this field to track promotion lines
                        })
                        total_qty -= order.promotion_id.min_quantity



                #total_qty = sum(lines.mapped('product_uom_qty'))
                #total_price = sum(lines.mapped('price_subtotal'))
                #if total_qty >= 100:


                #promotion_product = self.env.ref('category_promotion.promotion_discount_product')
                #'product_uom_qty': 1,
                #'product_uom': promotion_product.uom_id.id,







    #def _get_lines_group_by_category(self):
    #    for order in self:
    #        for line in order.order_line:
    ##            category = line.product_template_id.categ_id.id
    #            qty_per_category = line.product_uom_qty
    #            price_per_category = line.price_subtotal
    ##            for line2 in order.order_line:
      #              if line2.product_template_id.categ_id.id == category:
     #                   qty_per_category += line2.product_uom_qty
     #                   price_per_category += line2.price_subtotal
     #                   if qty_per_category >= 100:
                            



    #def add_promotion(self):
    #    for rec in self:
    #        return