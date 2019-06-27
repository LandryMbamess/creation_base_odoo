# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolClassroom(models.Model):
    _name = 'school.classroom'
    # champs simples
    name = fields.Char(string="Nom", required=True, )
    code = fields.Char(string="Code", )
    capacitance = fields.Integer(string="Capacité", required=False, )
    # champs relationnels

    professor_ids = fields.Many2many(comodel_name="school.professor", )
    student_ids = fields.One2many(comodel_name="school.student", inverse_name="classroom_id",)
    course_ids = fields.Many2many(comodel_name="school.course",)

    # cap_effectif = fields.Integer(compute='num_student', string="Nombre d'Etudiant")

    #
    # @api.depends('student_ids')
    # def num_student(self):
    #     self.cap_effectif = len(self.student_ids)
    #
    # @api.onchange('cap_effectif')
    # def cond_effectif(self):
    #     self.ensure_one()
    #     for rec in self:
    #         if rec.cap_effectif > rec.capacitance:
    #             return {'warning': {'title': 'Avertissement',
    #                                 'message': "le nombre d'etudiant excède déjà la capacité requise de la classe"}}
    #
