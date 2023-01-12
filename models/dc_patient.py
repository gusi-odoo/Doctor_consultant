from odoo import fields, models, api


class DCPatient(models.Model):
    _name = "dc.patient"
    _description = "Patient Model"

    name = fields.Char(string='Patient Name', required=True)
    address = fields.Char(string='Address')
    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default="male")
    phone = fields.Char(string='Phone', required=True)
    age = fields.Integer(string='Age', required=True)
    email = fields.Char(string='Email')
    patient_appointment_ids = fields.One2many(
        'dc.appointment', 'patient_id', string="Appointment Count", readonly=True)
