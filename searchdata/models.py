from django.db import models

# Create your models here.


class FIFARanking(models.Model):
    rank = models.IntegerField()
    country_full = models.CharField(max_length=64)
    country_abrv = models.CharField(max_length=16)
    total_points = models.DecimalField(max_digits=16, decimal_places=2)
    previous_points = models.IntegerField()
    rank_change = models.IntegerField()
    cur_year_avg = models.DecimalField(max_digits=16, decimal_places=2)
    cur_year_avg_weighted = models.DecimalField(max_digits=16, decimal_places=2)
    last_year_avg = models.DecimalField(max_digits=16, decimal_places=2)
    last_year_avg_weighted = models.DecimalField(max_digits=16, decimal_places=2)
    two_year_ago_avg = models.DecimalField(max_digits=16, decimal_places=2)
    two_year_ago_weighted = models.DecimalField(max_digits=16, decimal_places=2)
    three_year_ago_avg = models.DecimalField(max_digits=16, decimal_places=2)
    three_year_ago_weighted = models.DecimalField(max_digits=16, decimal_places=2)
    confederation = models.CharField(max_length=16)
    rank_date = models.CharField(max_length=16)

    class Meta:
        db_table = 'fifa_ranking'
