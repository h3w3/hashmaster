from django.db import models

class StatsYear(models.Model):
    year = models.IntegerField(primary_key=True)
    year_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hash_cash = models.FloatField()
    class Meta:
        db_table = 'stats_year'
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
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=25)
    zip_postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    mugshot = models.ImageField
    hash_cash_balance = models.FloatField()
    hash_cash_exempt = models.BooleanField()
    def __str__(self):
        return self.hash_name

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_description = models.CharField(max_length=255)
    hash_cash_exempt = models.BooleanField()
    def __str__(self):
        return self.role_name

class StatsYearRoles(models.Model):
    stats_year_id = models.ForeignKey(StatsYear, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    office_holder = models.ForeignKey(Hasher, on_delete=models.CASCADE)
    class Meta:
        db_table = 'stats_year_role'
        verbose_name_plural = "Stats year roles"  # Prevents "Newss" in the admin
    def __str__(self):
        return self.role_id.role_name

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    stats_year_id = models.ForeignKey(StatsYear, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=100)
    award_description = models.CharField(max_length=255)
    num_trails = models.IntegerField()
    def __str__(self):
        return self.award_name

class Trail(models.Model):
    trail_id = models.IntegerField(primary_key=True)
    stats_year_id = models.ForeignKey(StatsYear, on_delete=models.CASCADE)
    trail_date = models.DateField()
    trail_description = models.CharField(max_length=255)
    trail_start = models.TimeField()
    trail_start_location = models.CharField(max_length=255)
    checks = models.TextField()
    trail_end = models.TimeField()
    trail_end_location = models.CharField(max_length=255)
    map = models.ImageField()
    trash = models.FileField(upload_to='trails/trash')
    video = models.FileField(upload_to='trails/video')
    distance_turkey = models.FloatField()
    distance_eagle = models.FloatField()
    temperature = models.FloatField()
    visitors = models.ManyToManyField(Hasher, related_name='trail_visitors')
    namings = models.ManyToManyField(Hasher, related_name='trail_namings')
    cases = models.FloatField()
    published_in_stats = models.BooleanField()
    def __str__(self):
        return str(self.trail_id)

class Pack(models.Model):
    trail_id = models.ForeignKey(Trail, on_delete=models.CASCADE)
    hasher_id = models.ForeignKey(Hasher, on_delete=models.CASCADE)
    name_at_trail = models.CharField(max_length=255)
    hare = models.BooleanField()
    def __str__(self):
        return str(self.trail_id)