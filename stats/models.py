from contextlib import nullcontext

from django.db import models

class StatsYear(models.Model):
    year = models.IntegerField(primary_key=True)
    year_name = models.CharField(max_length=69)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hash_cash = models.FloatField()
    class Meta:
        db_table = 'stats_year'
    def __str__(self):
        return self.year_name

class HasherStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    description = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Hasher statuses"  # Prevents "Newss" in the admin
    def __str__(self):
        return self.name

class Hasher(models.Model):
    id = models.AutoField(primary_key=True)
    hash_name = models.CharField(max_length=69)
    nerd_first = models.CharField(max_length=30)
    nerd_last = models.CharField(max_length=30)
    hash_nickname = models.CharField(max_length=30)
    just_name = models.CharField(max_length=30)
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = models.CharField(
    #     max_length=1,
    #     choices=GENDER_CHOICES,
    #     blank=True,  # Allows the field to be empty if the user doesn't select one
    #     null=False,   # Allows the field to be empty in the database
    #     verbose_name="Gender"
    # )
    home_kennel = models.CharField(max_length=30)
    current_kennel = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=False)
    # phone = models.CharField(max_length=30, blank=True, null=False)
    address = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=50, blank=True, null=False)
    state_province = models.CharField(max_length=25, blank=True, null=False)
    zip_postal_code = models.CharField(max_length=10, blank=True, null=False)
    country = models.CharField(max_length=50, blank=True, null=False)
    mugshot = models.ImageField(upload_to='mugshots', blank=True, null=False)
    # first_trail = models.ForeignKey('Trail', on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(HasherStatus, on_delete=models.SET_NULL, null=True)
    hash_cash_balance = models.FloatField()
    hash_cash_exempt = models.BooleanField(blank=True, null=False, default=False)
    # pi_visible= models.BooleanField(blank=True, null=False, default=False)  # personal info visible
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
    trail_description = models.CharField(max_length=255, blank=True, null=False)
    trail_start = models.TimeField(blank=True, null=True)
    trail_start_location = models.CharField(max_length=255, blank=True, null=False)
    checks = models.TextField(blank=True, null=False)
    trail_end = models.TimeField(blank=True, null=True)
    trail_end_location = models.CharField(max_length=255, blank=True, null=False)
    map = models.FileField(upload_to='trails/map', blank=True, null=False)
    trash = models.FileField(upload_to='trails/trash', blank=True, null=False)
    video = models.FileField(upload_to='trails/video', blank=True, null=False)
    distance_turkey = models.FloatField(blank=True, null=False, default=0)
    distance_eagle = models.FloatField(blank=True, null=False, default=0)
    #distance_comment = models.CharField(max_length=255)   # Overview of trail from  Hash Statistician
    temperature = models.FloatField(blank=True, null=True)
    visitors = models.ManyToManyField(Hasher, related_name='trail_visitors', blank=True, null=False)
    namings = models.TextField(blank=True, null=False)
    cases = models.FloatField(blank=True, null=False, default=0)
    published_in_stats = models.BooleanField()  # check yes when trail stats final for public use
    def __str__(self):
        return str(self.trail_id)

class Pack(models.Model):
    trail_id = models.ForeignKey(Trail, on_delete=models.CASCADE)
    hasher_id = models.ForeignKey(Hasher, on_delete=models.CASCADE)
    name_at_trail = models.CharField(max_length=255) # accounts for name changes
    hare = models.BooleanField(default=False)        # check yes if hare
    #wanker = models.BooleanField(default=False)      # check yes if auto-wanker
    #transplant = models.BooleanField(default=False)  # check yes if transplant
    def __str__(self):
        return str(self.trail_id)

class TrailPhoto(models.Model):
    trail_id = models.ForeignKey(Trail, on_delete=models.CASCADE)
    attribution = models.ForeignKey(Hasher, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='trails/photos')
    caption = models.CharField(max_length=255, blank=True, null=False)
    def __str__(self):
        if self.photo:
            return self.photo.url
        return f"No image for {self.caption}"