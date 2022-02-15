from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError
import re

class HmsPatient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'
    _sql_constraints = [
        ('email_unique_constraint', 'UNIQUE(email)', 'This email already exists')
    ]


    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    email = fields.Char()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),('b', 'B'),('ab', 'AB'),('o', 'O')
    ], string='blood_type')
    pcr = fields.Boolean()
    image = fields.Image( max_width=100, max_height=100)
    adress = fields.Text()
    age = fields.Integer(compute='_calc_patient_age')
    logs_history = fields.One2many(comodel_name="hms.logs", inverse_name="patient_id")
    state = fields.Selection([
        ('Default', 'Default'),
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious'),
        ],default='Default')

    departments_id=fields.Many2one('hms.departments')
    doctor_id=fields.Many2many('hms.doctors','doctor_patient')
    Capacity=fields.Integer(related="departments_id.Capacity")

    def _calc_patient_age(self):
        for rec in self:
            if self.birth_date:
                rec.age = date.today().year - (rec.birth_date.year or 10)
            else:
                rec.age = 0


    @api.onchange('birth_date')
    def _birth_date_onchange(self):
        if self.birth_date:
            self.age=date.today().year-self.birth_date.year
            if self.age <= 30:
                self.pcr = True
                return {
                    'warning': {
                        'title': 'Alert',
                        'message': 'PCR has been check '
                    }

                }
    def Undetermined(self):
        self.state='Undetermined'
        self.env['hms.logs'].create({
            'description': f'State changed to {self.state}',
            'patient_id': self.id
        })

    def Good(self):
        self.state = 'Good'
        self.env['hms.logs'].create({
            'description': f'State changed to {self.state}',
            'patient_id': self.id
        })

    def Fair(self):
        self.state = 'Fair'
        self.env['hms.logs'].create({
            'description': f'State changed to {self.state}',
            'patient_id': self.id
        })

    def Serious(self):
        self.state = 'Serious'
        self.env['hms.logs'].create({
            'description': f'State changed to {self.state}',
            'patient_id': self.id
        })
    
    @api.model
    def create(self, vals_list):
        record = super().create(vals_list)
        self.env['hms.logs'].create({
            'description': 'Created Patient',
            'patient_id': record.id
        })
        return record

    @api.constrains('email')
    def _check_email(self):
        if self.email:
            if re.fullmatch(r"[a-zA-z0-9]+@[a-zA-z]+\.[a-zA-Z]+", str(self.email)) == None:
                raise ValidationError("Please Enter a Valid Email.")

                
