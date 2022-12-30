from odoo import api, fields, models, tools, _


class BackUpdateWizard(models.TransientModel):
    _name = "backupdate.wizard"
    _description = "back update "
    # _inherit = 'res.partner'

    discount_code = fields.Char(String='giam gia')
    partner_ids = fields.Many2many('res.partner')

    def update_wizard(self):
        # rentModel = self.env['res.partner']
        # for i in self:
        #     for j in i.discount_code:
        #         rentModel.create({'discount_code': i.discount_code} )
        self.partner_ids.write({'discount_code': self.discount_code})


        # def multi_update(self):
        #     ids = self.env.context['active_ids']
        #     rentModel = self.env['res.partner'].browes(ids)
        #
        #     new_data = {}
        #
        #     if self.discount_code:
        #         new_data["discount_code"]=self.discount_code

        # rentModel.write(new_data)
