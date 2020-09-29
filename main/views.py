from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Log, Aircraft, Airport, People
from .forms import AircraftForm, AirportForm, PeopleForm, LogForm


def logbook_overview(request):
    logs = Log.objects.all()
    return render(request, 'logs/logbook_overview.html', {'logs': logs})


def add_log(request):
    logs = Log.objects.all()
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogForm
        return render(request, 'logs/logbook_overview.html', {'logs': logs})
    return render(request, "adds/add_log.html", {"form": form})


def edit_log(request, pk):
    logs = Log.objects.get(id=pk)
    form = LogForm(instance=logs)
    if request.method == 'POST':
        form = LogForm(request.POST, instance=logs)
        if form.is_valid():
            form.save()
            return redirect('/logbook/')

    context = {"form": form}
    return render(request, "adds/add_log.html", context)


def logbook_details(request, logbook_id):
    entry = get_object_or_404(Log, id=logbook_id)
    return render(request, "logs/logbook_details.html", {"entry": entry})


def more(request):
    return render(request, "logs/more.html")


def aircraft(request):
    all_planes = Aircraft.objects.all()
    return render(request, "logs/aircraft.html", {"all_planes": all_planes})


def add_aircraft(request):
    all_planes = Aircraft.objects.all()
    form = AircraftForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AircraftForm
        return render(request, "logs/aircraft.html", {"all_planes": all_planes})
    return render(request, "adds/add_aircraft.html", {"form": form})


def edit_aircraft(request, pk):
    all_planes = Aircraft.objects.get(id=pk)
    form = AircraftForm(instance=all_planes)
    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=all_planes)
        if form.is_valid():
            form.save()
            return redirect('/logbook/aircraft/')

    context = {"form": form}
    return render(request, "adds/add_aircraft.html", context)


def airports(request):
    all_airports = Airport.objects.all()
    return render(request, "logs/airports.html", {"all_airports": all_airports})


def add_airport(request):
    all_airports = Airport.objects.all()
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AirportForm
        return render(request, "logs/airports.html", {"all_airports": all_airports})
    return render(request, "adds/add_airport.html", {"form": form})


def edit_airport(request, pk):
    all_airports = Airport.objects.get(id=pk)
    form = AirportForm(instance=all_airports)
    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=all_planes)
        if form.is_valid():
            form.save()
            return redirect('/logbook/airport/')

    context = {"form": form}
    return render(request, "adds/add_airport.html", context)


def people(request):
    all_people = People.objects.all()
    return render(request, "logs/people.html", {"all_people": all_people})


def add_people(request):
    all_people = People.objects.all()
    form = PeopleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PeopleForm
        return render(request, "logs/people.html", {"all_people": all_people})
    return render(request, "adds/add_people.html", {"form": form})


def edit_people(request, pk):
    all_people = People.objects.get(id=pk)
    form = PeopleForm(instance=all_people)
    if request.method == 'POST':
        form = PeopleForm(request.POST, instance=all_people)
        if form.is_valid():
            form.save()
            return redirect('/logbook/people/')

    context = {"form": form}
    return render(request, "adds/add_people.html", context)
