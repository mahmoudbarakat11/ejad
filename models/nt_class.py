from odoo import models , fields, api
from odoo.exceptions import ValidationError, UserError

class NtClass(models.Model):
    _name = "nt.class"
    # _inherits = {
    #     "nt.school": "school_ids"
    # }

    name = fields.Char()
    capacity = fields.Integer()
    student_ids = fields.One2many("nt.student", "class_id", string="Student")
    teacher_ids = fields.Many2many("nt.teacher", string="Teacher")
    school_ids = fields.Many2one("nt.school")
    description = fields.Text()

    @api.constrains('capacity')
    def check_capacity(self):
        if self.capacity > 40:
            raise ValidationError("the capacity can't be bigger than 40")


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name :
            domain = ['|',('capacity',operator,name),('description',operator,name)]
        return self._search(domain + args, limit= limit, access_rights_uid= name_get_uid)





