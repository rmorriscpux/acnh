from django.shortcuts import render
from django.db.models import Count
from .models import Bug, Fish, SeaCreature, Month, Hour, Shadow

def index(request):
    return render(request, "index.html")

def bugs(request):
    context = {}
    if request.method == "POST":
        # Get all the bugs for a selected month, or all if no month was selected.
        if 'selected_month' in request.POST:
            selected_month = Month.objects.filter(name=request.POST['selected_month'])
            if selected_month:
                month_bugs = selected_month[0].bugs.all()
                context['current_month'] = request.POST['selected_month']
            else:
                month_bugs = Bug.objects.all()
                context['current_month'] = ""
        else:
            month_bugs = Bug.objects.all()
        # Get all the bugs for a selected hour, or all if no hour was selected.
        if 'selected_hour' in request.POST:
            selected_hour = Hour.objects.filter(time=request.POST['selected_hour'])
            if selected_hour:
                hour_bugs = selected_hour[0].bugs.all()
                context['current_hour'] = selected_hour[0].time_am_pm
            else:
                hour_bugs = Bug.objects.all()
                context['current_hour'] = ""
        else:
            hour_bugs = Bug.objects.all()
        # Put them together.
        context['bugs'] = month_bugs.intersection(hour_bugs)
    else: # Grab all the bugs in the list.
        context['bugs'] = Bug.objects.all()
        context['current_month'] = ""
        context['current_hour'] = ""
    context['months'] = Month.objects.all()
    context['hours'] = Hour.objects.all()
    return render(request, "bugs.html", context)
    
def fish(request):
    context = {}
    if request.method == "POST":
        # Get all the fish for a selected shadow, or all if no shadow was selected.
        if 'selected_shadow' in request.POST:
            selected_shadow = Shadow.objects.filter(size=request.POST['selected_shadow'])
            if selected_shadow:
                shadow_fishes = selected_shadow[0].fishes.all()
                context['current_shadow'] = request.POST['selected_shadow']
            else:
                shadow_fishes = Fish.objects.all()
                context['current_shadow'] = ""
        else:
            shadow_fishes = Fish.objects.all()
        # Get all the bugs for a selected month, or all if no month was selected.
        if 'selected_month' in request.POST:
            selected_month = Month.objects.filter(name=request.POST['selected_month'])
            if selected_month:
                month_fishes = selected_month[0].fishes.all()
                context['current_month'] = request.POST['selected_month']
            else:
                month_fishes = Fish.objects.all()
                context['current_month'] = ""
        else:
            month_fishes = Fish.objects.all()
        # Get all the fish for a selected hour, or all if no hour was selected.
        if 'selected_hour' in request.POST:
            selected_hour = Hour.objects.filter(time=request.POST['selected_hour'])
            if selected_hour:
                hour_fishes = selected_hour[0].fishes.all()
                context['current_hour'] = selected_hour[0].time_am_pm
            else:
                hour_fishes = Fish.objects.all()
                context['current_hour'] = ""
        else:
            hour_fishes = Fish.objects.all()
        # Put them together.
        context['fishes'] = month_fishes.intersection(hour_fishes, shadow_fishes)
    else: # Grab all the fish in the list.
        context['fishes'] = Fish.objects.all()
        context['current_month'] = ""
        context['current_hour'] = ""
    context['months'] = Month.objects.all()
    context['hours'] = Hour.objects.all()
    context['shadows'] = Shadow.objects.all()
    return render(request, "fish.html", context)
    
def sea_creatures(request):
    context = {}
    if request.method == "POST":
        # Get all the sea creatures for a selected shadow, or all if no shadow was selected.
        if 'selected_shadow' in request.POST:
            selected_shadow = Shadow.objects.filter(size=request.POST['selected_shadow'])
            if selected_shadow:
                shadow_creatures = selected_shadow[0].sea_creatures.all()
                context['current_shadow'] = request.POST['selected_shadow']
            else:
                shadow_creatures = SeaCreature.objects.all()
                context['current_shadow'] = ""
        else:
            shadow_creatures = SeaCreature.objects.all()
        # Get all the bugs for a selected month, or all if no month was selected.
        if 'selected_month' in request.POST:
            selected_month = Month.objects.filter(name=request.POST['selected_month'])
            if selected_month:
                month_creatures = selected_month[0].sea_creatures.all()
                context['current_month'] = request.POST['selected_month']
            else:
                month_creatures = SeaCreature.objects.all()
                context['current_month'] = ""
        else:
            month_creatures = SeaCreature.objects.all()
        # Get all the sea creatures for a selected hour, or all if no hour was selected.
        if 'selected_hour' in request.POST:
            selected_hour = Hour.objects.filter(time=request.POST['selected_hour'])
            if selected_hour:
                hour_creatures = selected_hour[0].sea_creatures.all()
                context['current_hour'] = selected_hour[0].time_am_pm
            else:
                hour_creatures = SeaCreature.objects.all()
                context['current_hour'] = ""
        else:
            hour_creatures = SeaCreature.objects.all()
        # Put them together.
        context['sea_creatures'] = month_creatures.intersection(hour_creatures, shadow_creatures)
    else: # Grab all the sea creatures in the list.
        context['sea_creatures'] = SeaCreature.objects.all()
        context['current_month'] = ""
        context['current_hour'] = ""
    context['months'] = Month.objects.all()
    context['hours'] = Hour.objects.all()
    context['shadows'] = Shadow.objects.annotate(Count('sea_creatures')).filter(sea_creatures__count__gt=0)
    return render(request, "sea_creatures.html", context)