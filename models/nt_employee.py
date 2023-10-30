from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, UserError

class NtEmployee(models.Model):

    _name = 'nt.employee'

    name = fields.Char()
    age = fields.Integer()
    address = fields.Text()
    salary = fields.Integer()
    date = fields.Date()
    gender = fields.Selection(
        [('Male','male'), ('femle', 'femle')]
    )

    @api.constrains('age')
    def check_age(self):
        if self.age > 40:
            raise ValidationError(_("the capacity can't be bigger than 40"))



    # @api.returns('self', lambda x : x.id)
    # def copy(self, default=None):
    #     if not default:
    #         default = {}
    #         default['name'] = self.name + "(copy)"
    #         return super(NtEmployee,self).copy(default=default)


    def unlink(self):
        for rec in self:
            if rec.age > 30 :
                raise ValidationError('you cant delete this record')
        return super(NtEmployee,self).unlink()



