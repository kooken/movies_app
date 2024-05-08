from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=200, verbose_name='Movie name')
    movie_description = models.TextField(verbose_name='Movie description')
    movie_year = models.CharField(max_length=4, verbose_name='Movie year')
    movie_actors = models.TextField(verbose_name='Movie actors')
    movie_rating = models.FloatField(verbose_name='Movie rating')


    def __str__(self):
        return f'{self.movie_name} {self.movie_year} {self.movie_rating}'

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'