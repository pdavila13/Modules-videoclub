# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Item(models.Model):
    _name = 'videoclub.item'

    code = fields.Integer()
    numCopy = fields.Integer()
    type = fields.Text()
    gender = fields.Text()

class Movie(models.Model):
    _name = 'videoclub.movie'

    title = fields.Text()
    director = fields.Text()
    year = fields.Char(string="Year film", required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in minutes")
    movie_ids = fields.Many2many('res.partner', string="Movies")
    active = fields.Boolean(default=True)