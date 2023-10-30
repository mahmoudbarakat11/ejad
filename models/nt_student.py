from odoo import models, fields, api
from datetime import date, datetime
class NtStudent(models.Model):
    _name = "nt.student"


    name = fields.Char(string="Name", required=True)
    age = fields.Integer()
    state = fields.Selection(
        [('prim', 'primary'), ('sec', 'secondary'),('uni', 'university'),('dip','diploma')],
        string="grade", default="prim"
    )
    gender = fields.Selection(
        [('m', 'male'), ('f', 'female')]
    )
    active = fields.Boolean()
    class_id = fields.Many2one("nt.class", string="Class")
    capacity = fields.Integer(related="class_id.capacity", string="Capacity")

    def change_state(self):
         if self.state == 'prim':
             self.state = 'sec'
         elif self.state == 'sec':
             self.state = 'uni'
         elif self.state == 'uni':
             self.state = 'dip'



    # _sql_constraints = [
    #     ('check_field_name', 'unique (name)', 'this is name already exist')
    # ]

    # _sql_constraints = [
    #     ('check_field_age', 'check (age > 20)', 'the age must be bigger than 20'),
    # ]


    def print_record(self):
        domain = [('age', '>', 30)]

        filitred_record = (self.env['nt.student'].search(domain))
        for rec in filitred_record:
            rec.name = "old student"
