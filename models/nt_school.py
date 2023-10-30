from odoo import models,fields,api

class NtSchool(models.Model):
    _name = "nt.school"

    name = fields.Char()
    grade = fields.Selection(
        [('prim', 'primary'), ('sec', 'secondary')]
    )

    my_text = fields.Text(string="Created By")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', "name already exists")
    ]

    class_id = fields.One2many("nt.class", "school_ids")

    # def print_rec(self):
    #     for rec in self:
    #         rec.my_text = self.env['nt.student'].search([('age','>=',10)])


    def print_record(self):
        print(">>>>>>>>>>>>>>>>>>>>>>",self.env['nt.school'].search_count([]))






