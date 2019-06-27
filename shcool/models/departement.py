# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolDepartement(models.Model):
    _name = 'school.departement'

    name = fields.Char(string="Nom", required=True, )
    code = fields.Char(string="Code", )

    professor_ids = fields.One2many(comodel_name="school.professor", inverse_name="departement_id", readonly=True)
    student_ids = fields.One2many(comodel_name="school.student", inverse_name="departement_id", readonly=True)
    course_ids = fields.One2many(comodel_name="school.course", inverse_name="departement_id", readonly=True)


