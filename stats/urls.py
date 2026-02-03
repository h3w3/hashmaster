from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trails/", views.trails, name="trails"),
    path("trails/<int:trail_id>/", views.trail, name="trail"),
    path("trails/<int:trail_id>/map/", views.map, name="map"),
    path("trails/<int:trail_id>/pack/", views.pack, name="pack"),
    path("trails/<int:trail_id>/trash/", views.trash, name="trash"),
    path("trails/<int:trail_id>/hares/", views.hares, name="hares"),
    path("trails/<int:trail_id>/video/", views.video, name="video"),
    path("hashers/", views.hashers, name="hashers"),
    path("hashers/<int:id>/", views.hasher, name="hasher"),
    path("hashers/<str:hasher_name>/", views.hasher_name, name="hasher_name"),
    path("years/", views.stats_years, name="stats_years"),
    path("years/<int:year>/", views.stats_year, name="stats_year"),
    path("awards/", views.awards, name="awards"),
    path("awards/<int:num_trails>/", views.award, name="award"),

]