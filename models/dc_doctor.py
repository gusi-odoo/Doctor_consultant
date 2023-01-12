from odoo import fields, api, models


class DCDoctor(models.Model):
    _name = "dc.doctor"
    _description = "Doctor Model"

    name = fields.Char(string='Doctor Name', required=True)
    address = fields.Char(string='Address')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)
    age = fields.Integer(string='Age', required=True)
    status = fields.Selection(
        [('fulltime', 'Full time'), ('parttime', 'Part time')], required=True, default='fulltime')
    description = fields.Text()
    joined_from = fields.Date(string='Joined Date')
    image = fields.Binary(string='Image', attachment=True)
    view_appointment_ids = fields.One2many(
        'dc.appointment', 'appointed_doctor_id', string="Appointment Count", readonly=True)
