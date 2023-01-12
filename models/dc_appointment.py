from odoo import fields, models, api


class DCAppointment(models.Model):
    _name = "dc.appointment"
    _description = "Appointments for patient"

    name = fields.Char(string='Appointment Reference',
                       required=True, copy=False, readonly=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    age = fields.Integer(string='Age')
    description = fields.Text()
    note = fields.Text()
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), (
        'done', 'Done'), ('cancel', 'Canceled')], default='draft', required=True)
    appointment_date = fields.Datetime(
        string='Appointment Date', default=fields.datetime.now())
    appointed_doctor_id = fields.Many2one(
        "dc.doctor", string="Doctor name", required=True)
    patient_id = fields.Many2one(
        "dc.patient", string='Patient Name', required=True)
