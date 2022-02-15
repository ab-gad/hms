from odoo import models, fields


class HmsDepartments(models.Model):
    _name = 'hms.departments'
    _rec_name = 'name'

    name = fields.Char()
    Capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients_ids = fields.One2many('hms.patient', 'departments_id')
