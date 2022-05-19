from odoo import fields, models, api
import datetime


class SchedulerReport(models.Model):
    _name = 'scheduler.report'
    _description = 'scheduler.report'


    def generate_scheduled_report(self):
        print("hello")