# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = 'school.professor'
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
    date = fields.Datetime(string="Date recrutement", default=fields.Datetime.now(), )
    date_start = fields.Datetime(string="Date de debut", default=fields.Datetime.now(), )
    state = fields.Selection(string="Status", selection=[('T1', 'Titulaire'), ('T2', 'Vacataire'),
                                                         ('T3', 'Administration'), ], default='T1',
                             track_visibility='onchange')
    active = fields.Boolean(string="Actif", default=True)

    # champs relationnel
    course_ids = fields.Many2many(comodel_name="school.course", )
    departement_id = fields.Many2one(comodel_name="school.departement", string="Departement",)
    classroom_ids = fields.Many2many(comodel_name="school.classroom",)

    @api.multi
    def statu_titulaire(self):
        self.state = 'T1'

    @api.multi
    def statu_vacataire(self):
        self.state = 'T2'

    @api.multi
    def statu_administration(self):
        self.state = 'T3'


    @api.multi
    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('shcool.email_template_prof').id
        ctx = {
            'default_model': 'school.professor',
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
