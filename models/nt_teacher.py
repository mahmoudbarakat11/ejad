from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime


class NtTeacher(models.Model):
    _name = "nt.teacher"

    name = fields.Char()
    age = fields.Integer(compute="_calc_age")
    date = fields.Date()
    class_ids = fields.Many2many("nt.class", string="Class")
    special_class_ids = fields.Many2many("nt.class", "class_teacher"
                                                     "class_ids", "teacher_ids", string="Special Class")
    salary = fields.Integer(string="Salary")
    tax = fields.Float(compute="calc_tax", string="Tax")


    @api.depends('salary')
    def calc_tax(self):
        self.tax = self.salary * 0.10

    @api.onchange('age')
    def change_age(self):
        if self.age >= 40:
            self.salary = 2000
        else:
            self.salary = 1000

    @api.depends('date')
    def _calc_age(self):
        for rec in self:
            if rec.date:
                rec.age = rec.date.today().year - rec.date.year
            else:
                rec.age = 1

