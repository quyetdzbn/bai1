from pkg_resources import _

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class ResPartnerInherit(models.Model):
    # _name = 'customer'
    _description = 'giam gia'
    _inherit = 'res.partner'

    discount_code = fields.Char(String='giam gia')  # VIP_10
    sale_order_discount_estimated = fields.Char(String='uoc tinh', compute="total_discount_estimated")  # 10

    # name = fields.Char(String='ten', require=True)
    check1 = fields.Boolean(compute='check', store=True)

    # discount_estimated = fields.Integer()
    # discount_total = fields.Integer(compute='sale_order_discount_estimated1', store=True)
    #
    @api.depends('discount_code')
    def check(self):
        for i in self:
            i.check1 = False
            if i.discount_code:
                if len(i.discount_code.split('_')) > 1:
                    if i.discount_code.split('_')[0] == 'VIP' and int(i.discount_code.split('_')[1]) < 100:
                        i.check1 = True

    #
    @api.constrains('discount_code')
    def check_discount_code(self):
        for i in self:
            if not i.discount_code:
                raise ValidationError('You can not create discount_code.')
            if i.discount_code:
                if i.discount_code.find('_')<0:
                    raise ValidationError('You can not create discount_code.')


    @api.depends('discount_code')
    def total_discount_estimated(self):
        for i in self:
            i.sale_order_discount_estimated = 0
            if i.discount_code:
                if i.discount_code.split('_')[1]:
                    i.sale_order_discount_estimated = int(i.discount_code.split('_')[1])


    def update_code_customer(self):
        ids = [x.id for x in self]
        view_id = self.env.ref('bai1.view_back_update').id
        return {
            'type': 'ir.actions.act_window',
            'name': 'Update wizard',
            'view_mode': 'form',
            'view_id': view_id,
            'res_model': 'backupdate.wizard',
            'target': 'new',
            'context': {
                'default_partner_ids': [(6, 0, ids)],
            }
        }

    # @api.model
    # def create(self, values):
    #     if not self.user_has_groups('bai1.advance_sale'):
    #         if 'discount_code' in values:
    #             raise UserError(
    #                 'You are not allowed to modify '
    #                 'manager_remarks')
    #     return super(CustomField, self).create(values)
    #
    # def write(self, values):
    #     if not self.user_has_groups('bai1.advance_sale'):
    #         if 'discount_code' in values:
    #             raise UserError(
    #                 'You are not allowed to modify '
    #                 'manager_remarks')
    #     return super(CustomField, self).write(values)
