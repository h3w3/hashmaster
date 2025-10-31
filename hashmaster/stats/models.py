from django.db import models


class StatYear(models.Model):
    year = models.IntegerField()
    year_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'stats_year'
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hash_cash = models.FloatField()
    def __str__(self):
        return self.year_name


class Hasher(models.Model):
    id = models.AutoField(primary_key=True)
    hash_name = models.CharField(max_length=69)
    nerd_first = models.CharField(max_length=30)
    nerd_last = models.CharField(max_length=30)
    hash_nickname = models.CharField(max_length=30)
    just_name = models.CharField(max_length=30)
    home_kennel = models.CharField(max_length=30)
    current_kennel = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    def __str__(self):
        return self.hash_name
    address = models.TextField()
    city = models.TextField()
    state_province = models.TextField()
    zip_postal_code = models.TextField()
    country = models.TextField()
    mugshot = models.ImageField
    hash_cash_balance = models.FloatField()
    hash_cash_exampe = models.BooleanField()