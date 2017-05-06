from odoo import models, fields, api, _


class TerminateReason(models.TransientModel):
    _name = "terminate.reason"

    reason = fields.Text('Reason')

    @api.multi
    def save_terminate(self):
        '''Method to terminate student and change state to terminate'''
        self.env['student.student'].browse(self._context.get
                                          ('active_id')).write({
                                          'state': 'terminate',
                                          'terminate_reason': self.reason})
