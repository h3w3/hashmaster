from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from stats.models import Trail, TrailPhoto, Pack, HasherStatus
from stats.models import Hasher, Award, StatsYear

def index(request):
    recent_trails = Trail.objects.order_by("-trail_id")[:3]  # most recent 3 trails
    return render(request, "stats/index.html",{"recent_trails": recent_trails})

def trails(request):
    all_trails = Trail.objects.filter(published_in_stats=True).order_by("-trail_id") # all published trails by desc id
    return render(request, "stats/trails.html", {"all_trails": all_trails})

def trail(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    trail_photos = TrailPhoto.objects.filter(trail_id=trail_id)
    pack = Pack.objects.filter(trail_id=trail_id).order_by("name_at_trail")
    hares = Pack.objects.filter(trail_id=trail_id, hare=True)
    # wankers = Pack.objects.filter(trail_id=trail_id, wanker=True)
    # transplants = Pack.objects.filter(trail_id=trail_id, transplant=True)
    return render(request, "stats/trail.html", {"trail": trail, "hares": hares,
                                         "trail_photos": trail_photos ,"hashers": hashers,
                                         "pack": pack
                                       #  "wankers": wankers, "transplants": transplants})
                                                })

def map(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/map.html", {"trail": trail})

def pack(request, trail_id):
    pack = Pack.objects.filter(trail_id=trail_id)
    return render(request, "stats/pack.html", {"pack": pack, "trail": trail_id})

def trash(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/trash.html", {"trail": trail})

def hares(request, trail_id):
    hares = Pack.objects.filter(trail_id=trail_id, hare=True)
    return render(request, "stats/hares.html", {"hares": hares, "trail": trail_id})

def video(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/video.html", {"trail": trail})

def hashers(request):
    active_status = HasherStatus.objects.filter(abbreviation__in=["A", "L"])
    all_hashers = Hasher.objects.filter(status__in=active_status).order_by("hash_name")
    return render(request, "stats/hashers.html", {"all_hashers": all_hashers})

def hasher(request, id):
    hasher = get_object_or_404(Hasher, pk=id)
    hasher_trails = Pack.objects.filter(hasher_id= id)
    first_trail = Pack.objects.filter(hasher_id=id).first()
    latest_trail = Pack.objects.filter(hasher_id=id).latest("trail_id")
    hasher_status = HasherStatus.objects.filter(hasher=id).first
    return render(request, "stats/hasher.html", {"hasher": hasher, "hasher_trails": hasher_trails,
                                        "first_trail": first_trail, "latest_trail": latest_trail, "hasher_status": hasher_status})

def hasher_name(request, hasher_name):
    return HttpResponse("You're looking at the hasher with name %s." % hasher_name)

def stats_years(request):
    all_stats_years = StatsYear.objects.order_by("-year")
    return render(request, 'stats/stats_years.html', {"all_stats_years": all_stats_years})

def stats_year(request, year):
    return HttpResponse("You're looking at the annual stats for stats year %s." % year)

def awards(request):
    all_awards = Award.objects.order_by("num_trails")
    return render(request, "stats/awards.html", {"all_awards": all_awards})

def award(request, num_trails):
    return HttpResponse("You're looking at the award winners for %s trails." % num_trails)
