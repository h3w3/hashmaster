from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import views as auth_views
from stats.models import Trail, TrailPhoto, Pack, HasherStatus
from stats.models import Hasher, Award, StatsYear
from django.db.models import Count

def root(request):
    return HttpResponse("You're looking at the kennel root home page outside of Hashmaster")

def index(request):
    recent_trails = Trail.objects.order_by("-trail_id")[:3]  # most recent 3 trails
    recent_years = StatsYear.objects.order_by("-year")[:3]   # most recent 3 years
    return render(request, "stats/index.html",{"recent_trails": recent_trails,
                                                            "recent_years": recent_years })

def trails(request):
    all_trails = Trail.objects.filter(published_in_stats=True).order_by("-trail_id") # all published trails by desc id
    return render(request, "stats/trails.html", {"all_trails": all_trails})

def trail(request, trail_id):
    # Trail information
    trail = get_object_or_404(Trail, pk=trail_id)
    trail_photos = TrailPhoto.objects.filter(trail_id=trail_id)
    pack = Pack.objects.filter(trail_id=trail_id).order_by("name_at_trail")
    hares = Pack.objects.filter(trail_id=trail_id, hare=True)
    visitors = Pack.objects.filter(trail_id=trail_id, visitor=True)
    wankers = Pack.objects.filter(trail_id=trail_id, wanker=True)
    transplants = Pack.objects.filter(trail_id=trail_id, transplant=True)
    new_boots = Pack.objects.filter(trail_id=trail_id, new_boot=True)
    frb = Pack.objects.filter(trail_id=trail_id, frb=True)
    fbi = Pack.objects.filter(trail_id=trail_id, fbi=True)
    dfl = Pack.objects.filter(trail_id=trail_id, dfl=True)
    dnf = Pack.objects.filter(trail_id=trail_id, dnf=True)
    # Stats year to date aggregate
    ytd_longest = Trail.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by("-distance_turkey")[:3]
    ytd_shortest = Trail.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by("distance_turkey")[:3]
    #ytd_largest = Pack.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by(ytd_biggest.count)[:3]
    #ytd_smallest = Pack.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by("distance_turkey")[:3]
    ytd_warmest = Trail.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by("-temperature")[:3]
    ytd_coldest = Trail.objects.filter(stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id).order_by("temperature")[:3]
    ytd_frb = (Pack.objects.filter(trail_id__stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id, frb=True).values(
        'hasher_id', 'name_at_trail').annotate(count=Count('hasher_id'))).filter(count__gte=1)
    ytd_fbi = (
        Pack.objects.filter(trail_id__stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id, fbi=True).values(
        'hasher_id', 'name_at_trail').annotate(count=Count('hasher_id'))).filter(count__gte=1)
    ytd_dfl = (
        Pack.objects.filter(trail_id__stats_year_id=trail.stats_year_id, trail_id__lte=trail.trail_id, dfl=True).values(
            'hasher_id', 'name_at_trail').annotate(count=Count('hasher_id'))).filter(count__gte=1)
    return render(request, "stats/trail.html", {"trail": trail, "hares": hares,
                                         "trail_photos": trail_photos ,"hashers": hashers,
                                         "pack": pack,   "wankers": wankers, "visitors": visitors,
                                         "transplants": transplants, "new_boots": new_boots,
                                         "frb": frb, "fbi": fbi, "dfl": dfl, "dnf": dnf,
                                         "ytd_longest": ytd_longest, "ytd_shortest": ytd_shortest,
                                         "ytd_warmest": ytd_warmest, "ytd_coldest": ytd_coldest,
                                         "ytd_frb": ytd_frb, "ytd_fbi": ytd_fbi, "ytd_dfl": ytd_dfl  })

def map(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/map.html", {"trail": trail})

def pack(request, trail_id):
    pack = Pack.objects.filter(trail_id=trail_id).order_by("name_at_trail")
    trail_date = Trail.objects.get(pk=trail_id).trail_date
    return render(request, "stats/pack.html", {"pack": pack, "trail": trail_id,
                                        "trail_date": trail_date})

def trash(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/trash.html", {"trail": trail})

def hares(request, trail_id):
    hares = Pack.objects.filter(trail_id=trail_id, hare=True)
    trail_date = Trail.objects.get(pk=trail_id).trail_date
    return render(request, "stats/hares.html", {"hares": hares, "trail": trail_id,
                                        "trail_date": trail_date})

def video(request, trail_id):
    trail = get_object_or_404(Trail, pk=trail_id)
    return render(request, "stats/video.html", {"trail": trail})

def hashers(request):
    active_status = HasherStatus.objects.filter(abbreviation__in=["A", "L"])  # active or lost on trail
    all_hashers = Hasher.objects.filter(status__in=active_status).order_by("hash_name")
    return render(request, "stats/hashers.html", {"all_hashers": all_hashers})

# @login_required(login_url="/login/")
def hasher(request, id):
    hasher = get_object_or_404(Hasher, pk=id)
    hasher_trails = Pack.objects.filter(hasher_id= id)
    hared_trails = Pack.objects.filter(hasher_id=id, hare=True)
    first_trail = Pack.objects.filter(hasher_id=id).order_by('trail_id')[:1].get()
    latest_trail = Pack.objects.filter(hasher_id=id).latest("trail_id")
    wanked = Pack.objects.filter(hasher_id=id, wanker=True)
    hasher_status = HasherStatus.objects.filter(hasher=id).first
    return render(request, "stats/hasher.html", {"hasher": hasher, "hasher_trails": hasher_trails,
                                        "first_trail": first_trail, "latest_trail": latest_trail, "wanked": wanked,
                                        "hasher_status": hasher_status, "hared_trails": hared_trails})

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
