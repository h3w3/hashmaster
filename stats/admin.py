from django.contrib import admin
from .models import StatsYear, StatsYearRoles, HasherStatus, Hasher, Role, Award, Trail, Pack

class StatsYearRolesAdmin(admin.ModelAdmin):
    list_display = ('stats_year_id', 'role_id', 'office_holder')

class AwardAdmin(admin.ModelAdmin):
    list_display = ('num_trails', 'award_name', 'stats_year_id')

class TrailAdmin(admin.ModelAdmin):
    list_display = ('trail_id', 'trail_date', 'trail_description')

class PackAdmin(admin.ModelAdmin):
    list_display = ('trail_id', 'hasher_id', 'hare')

class HasherStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(StatsYear)
admin.site.register(StatsYearRoles, StatsYearRolesAdmin)
admin.site.register(HasherStatus, HasherStatusAdmin)
admin.site.register(Hasher)
admin.site.register(Role)
admin.site.register(Award, AwardAdmin)
admin.site.register(Trail, TrailAdmin)
admin.site.register(Pack, PackAdmin)
