from odoo import models, fields, api, _




class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'





    category_promotion_active = fields.Boolean(
        string="Category Promotions",
        help="Activate or deactivate the category promotions system",
        config_parameter='category_promotion.enable_promotions'
    )

    @api.model
    def set_values(self):
        super().set_values()

        # Reference the menus (set raise_if_not_found = False to avoid crash)
        menu_main = self.env.ref('category_promotion.menu_promotion', raise_if_not_found=False)

        # Read setting value
        is_active = self.category_promotion_active

        # Set menu visibility
        if menu_main:
            menu_main.active = is_active