# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Item(models.Model):
    _name = 'videoclub.item'

    code = fields.Integer()
    numCopy = fields.Integer()
    type = fields.Text()
    gender = fields.Text()

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Movie, self).copy(default)

    _sql_constrains = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the movie should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The movie title must be unique"),
    ]

class Movie(models.Model):
    _name = 'videoclub.movie'

    title = fields.Text()
    director = fields.Text()
    year = fields.Char(string="Year film", required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in minutes")
    movie_ids = fields.Many2many('res.partner', string="Movies")
    active = fields.Boolean(default=True)

@api.onchange('movies', 'movie_ids')
def _verify_valid_movies(self):
    if self.movies < 0:
        return {
            'warning': {
                'title': "Incorrent 'movies' value",
                'message': "The number of available movies many not be negative",
            },
        }

    if self.movies < len(self.movies_ids):
        return {
            'warning': {
                'title': "Too many movies",
                'message': "Increase movies or remove excess movies",
            },
        }