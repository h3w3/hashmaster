from django.contrib import admin
from .models import StatsYear, StatsYearRoles, HasherStatus, Hasher, Role, Award, Trail, Pack, TrailPhoto

class StatsYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'year_name', 'start_date')
    ordering = ['-year']

class StatsYearRolesAdmin(admin.ModelAdmin):
    list_display = ('stats_year_id', 'role_id', 'office_holder')
    ordering = ['-stats_year_id']

class AwardAdmin(admin.ModelAdmin):
    list_display = ('num_trails', 'award_name', 'stats_year_id')
    ordering = ['num_trails']

class TrailAdmin(admin.ModelAdmin):
    list_display = ('trail_id', 'trail_date', 'trail_description')
    ordering = ['-trail_id']

class PackAdmin(admin.ModelAdmin):
    list_display = ('trail_id', 'hasher_id', 'hare')
    ordering = ['trail_id']

class HasherAdmin(admin.ModelAdmin):
    list_display = ('hash_name', 'nerd_first', 'nerd_last', 'status', 'mugshot')
    ordering = ['hash_name']

class HasherStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ['name']

class TrailPhotoAdmin(admin.ModelAdmin):
     list_display = ('trail_id', 'caption', 'attribution', 'photo')

class RoleAdmin(admin.ModelAdmin):
     list_display = ('role_name', 'role_description')
     ordering = ['role_name']

admin.site.register(StatsYear, StatsYearAdmin)
admin.site.register(StatsYearRoles, StatsYearRolesAdmin)
admin.site.register(HasherStatus, HasherStatusAdmin)
admin.site.register(Hasher, HasherAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Trail, TrailAdmin)
admin.site.register(Pack, PackAdmin)
admin.site.register(TrailPhoto, TrailPhotoAdmin)
