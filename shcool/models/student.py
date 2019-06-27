# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = 'mail.thread'

    name = fields.Char(string="Nom", required=True)
    last_name = fields.Char(string="Prenom", )
    birthday = fields.Date(string="Date de naissance", required=False, )
    site = fields.Char(string="Lieu de naissace", required=False, )
    sex = fields.Selection(string="Genre", selection=[('Masculin', 'Masculin'),
                                                         ('Feminin', 'Feminin'), ], required=True, )
    identity = fields.Char(string="CNI", required=True, )
    address = fields.Char(string="Adresse", required=False, )
    email = fields.Char(string="Email",)
    phone = fields.Char(string="Tel",)
    image = fields.Binary(string="Image",)
    date = fields.Datetime(string="Date d'inscription", default=fields.Datetime.now(), )
    state = fields.Selection(string="Niveau", selection=[('L1', 'Licene1'),
                                                         ('L2', 'Licence2'), ('L3', 'Licence3'), ('M1', 'Master1'),
                                                         ('M2', 'Master2'), ], default='L1', track_visibility='onchange')
    # Champ relationnel
    classroom_id = fields.Many2one(comodel_name="school.classroom",)
    departement_id = fields.Many2one(comodel_name="school.departement",)
    course_ids = fields.Many2many(related='classroom_id.course_ids', readonly=True)



    @api.multi
    def next_level(self):
        self.ensure_one()
        if self.state == 'L1':
            return self.write({'state': 'L2'})
        elif self.state == 'L2':
            return self.write({'state': 'L3'})
        if self.state == 'L3':
            return self.write({'state': 'M1'})
        if self.state == 'M1':
            return self.write({'state': 'M2'})
        else:
            raise ValidationError("L'Etudiant est déjà en fin d'Etude")

    @api.multi
    def reset_level(self):
        for rec in self:
            rec.write({'state': 'L1'})

    @api.multi
    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('shcool.email_student_prof').id
        ctx = {
            'default_model': 'school.student',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.email,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
