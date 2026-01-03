from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're looking at the HashMaster stats index.")

def trails(request):
    return HttpResponse("You're looking at all the trails.")

def trail(request, trail_id):
    return HttpResponse("You're looking at stats for trail %s." % trail_id)

def map(request, trail_id):
    return HttpResponse("You're looking at the map for trail %s." % trail_id)

def pack(request, trail_id):
    return HttpResponse("You're looking at the pack for trail %s." % trail_id)

def trash(request, trail_id):
    return HttpResponse("You're looking at the trash for trail %s." % trail_id)

def hares(request, trail_id):
    return HttpResponse("You're looking at all the hares for trail %s." % trail_id)

def hashers(request):
    return HttpResponse("You're looking at all the active hashers")

def hasher_name(request, hasher_name):
    return HttpResponse("You're looking at the hasher with name %s." % hasher_name)

def stats_year(request, year):
    return HttpResponse("You're looking at the annual stats for stats year %s." % year)