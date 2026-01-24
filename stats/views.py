from django.http import HttpResponse
from django.template import loader
from stats.models import Trail
from stats.models import Hasher
from stats.models import Award
from stats.models import StatsYear

def index(request):
    recent_trails = Trail.objects.order_by("trail_id")[:3]  # most recent 3 trails
    template = loader.get_template("stats/index.html")
    context = {"recent_trails": recent_trails}
    return HttpResponse(template.render(context, request))

def trails(request):
    all_trails = Trail.objects.order_by("-trail_id")  # all trails by id
    template = loader.get_template("stats/trails.html")
    context = {"all_trails": all_trails}
    return HttpResponse(template.render(context, request))

def trail(request, trail_id):
    return HttpResponse("You're looking at stats for trail %i." % trail_id)

def map(request, trail_id):
    return HttpResponse("You're looking at the map for trail %s." % trail_id)

def pack(request, trail_id):
    return HttpResponse("You're looking at the pack for trail %s." % trail_id)

def trash(request, trail_id):
    return HttpResponse("You're looking at the trash for trail %s." % trail_id)

def hares(request, trail_id):
    return HttpResponse("You're looking at all the hares for trail %s." % trail_id)

def hashers(request):
    all_hashers = Hasher.objects.order_by("hash_name")
    template = loader.get_template("stats/hashers.html")
    context = {"all_hashers": all_hashers}
    return HttpResponse(template.render(context, request))

def hasher(request, id):
    return HttpResponse("You're looking at the hasher with id %i." % id)

def hasher_name(request, hasher_name):
    return HttpResponse("You're looking at the hasher with name %s." % hasher_name)

def stats_years(request):
    all_stats_years = StatsYear.objects.order_by("-year")
    template = loader.get_template("stats/stats_years.html")
    context = {"all_stats_years": all_stats_years}
    return HttpResponse(template.render(context, request))

def stats_year(request, year):
    return HttpResponse("You're looking at the annual stats for stats year %s." % year)

def awards(request):
    all_awards = Award.objects.order_by("num_trails")
    template = loader.get_template("stats/awards.html")
    context = {"all_awards": all_awards}
    return HttpResponse(template.render(context, request))

def award(request, num_trails):
    return HttpResponse("You're looking at the award winners for %s trails." % num_trails)
