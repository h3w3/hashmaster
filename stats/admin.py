from django.contrib import admin
from .models import StatsYear, StatsYearRoles, Hasher, Role, Award, Trail, Pack

class StatsYearRolesAdmin(admin.ModelAdmin):
    list_display = ('stats_year_id', 'role_id', 'office_holder')

admin.site.register(StatsYear)
admin.site.register(StatsYearRoles, StatsYearRolesAdmin)
admin.site.register(Hasher)
admin.site.register(Role)
admin.site.register(Award)
admin.site.register(Trail)
admin.site.register(Pack)

# Register your models here.
