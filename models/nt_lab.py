from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError
class NtLab(models.Model):
    _name = 'nt.lab'

    name = fields.Char(string="Name")
    age = fields.Integer()
    descriptions = fields.Char()
    date = fields.Date()
    state = fields.Selection(
        [('deraft', 'Deraft'),('ready', 'Ready'),('canceled','Canceled')]
    )
    # def my_create(self):
    #     record1 = {
    #         "name": "ali",
    #         "age": 40
    #     }
    #
    #     record2 = {
    #         "name": "mazen",
    #         "age": 6
    #     }
    #
    #     self.env['nt.lab'].create([record1, record2])
    #
    # @api.model
    # def create(self,vals):
    #     vals['name'] = self.env['ir.sequence'].next_by_code('lab sequence')
    #     return super(NtLab, self).create(vals)

    # def print_output(self):
    #     searched_lab = self.env['nt.lab'].search([])
    #     browsed_lab = self.env['nt.lab'].browse(searched_lab)
    #     filtered_lab = searched_lab.filtered(lambda rec :rec.age > 20)
    #     mapped_lab = searched_lab.mapped('age')
    #     sorted_lab = searched_lab.sorted('write_date')
    #
    #     print(">>>>>>>>>",searched_lab)
    #     print(">>>>>>>>>>",browsed_lab)
    #     print(">>>>>>>",filtered_lab)
    #     print(">>>>>>>>>>>", mapped_lab)
    #     print(">>>>>>>>>>>", sorted_lab)

    # def name_get(self):
    #     list = []
    #     for rec in self:
    #         name = rec.name +" " +rec.descriptions
    #         list.append((rec.id, name))
    #     return list

    # def name_get(self):
    #     for rec in self:
    #         return [(rec.id, "(%s) (%s)" % (rec.descriptions, rec.name))]


    # @api.model
    # def default_get(self, fields):
    #     res = super(NtLab, self).default_get(fields)
    #     res['age'] = 100
    #     res['date'] = date.today()
    #     print(fields)
    #     return res

    # def write(self,vals):
    #     print(vals)
    #     vals['descriptions'] = self.env.user.name
    #     return super(NtLab,self).write(vals)

    def unlink(self):
        for rec in self:
            if rec.state == 'ready':
                raise (ValidationError("you can't delete this record"))
        return super(NtLab, self).unlink()



