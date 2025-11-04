from django.contrib import admin
from .models import StatsYear, StatsYearRoles, Hasher, Role

admin.site.register(StatsYear)
admin.site.register(StatsYearRoles)
admin.site.register(Hasher)
admin.site.register(Role)

# Register your models here.
