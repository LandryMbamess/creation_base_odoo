# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolCourse(models.Model):
    _name = 'school.course'

    # champs simple
    name = fields.Char(string="Intitulé", required=True, )
    code = fields.Char(string="Code", )
    new_field = fields.Float(string="Dure en heure", digits=(2, 2), required=False, )
    #

    professor_ids = fields.Many2many(comodel_name="school.professor", )
    classroom_ids = fields.Many2many(comodel_name="school.classroom",)
    departement_id = fields.Many2one(comodel_name="school.departement", string="Departement", )

