from django.shortcuts import render, redirect
from .models import Event
from .models import Announcement, Circular, Broadcast
from .models import Club
from .forms import GrievanceForm, SuggestionForm
from .forms import ContributeForm
from .models import Contribution


def contribute(request):
    if request.method == 'POST':
        form = ContributeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contribute_success')  # Redirect to a success page
    else:
        form = ContributeForm()
    return render(request, 'contribute.html', {'form': form})


def contribute_success(request):
    return render(request, 'contribute_success.html')


def home(request):
    return render(request, 'home.html')


def clubs_page(request):
    clubs = Club.objects.all()
    return render(request, 'clubs.html', {'clubs': clubs})


def gallery(request):
    return render(request, 'gallery.html')


def announcements_view(request):
    announcements = Announcement.objects.all()
    circulars = Circular.objects.all()
    broadcasts = Broadcast.objects.all()
    return render(request, 'acb.html', {'announcements': announcements, 'circulars': circulars, 'broadcasts': broadcasts})


def circulars_view(request):
    circulars = Circular.objects.all()
    return render(request, 'circulars.html', {'circulars': circulars})


def broadcasts_view(request):
    broadcasts = Broadcast.objects.all()
    return render(request, 'broadcasts.html', {'broadcasts': broadcasts})

# def add_announcement(request):
#     if request.method == 'POST':
#         form = AnnouncementForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('announcements')
#     else:
#         form = AnnouncementForm()
#     return render(request, 'add_announcement.html', {'form': form})

# def add_circular(request):
#     if request.method == 'POST':
#         form = CircularForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('circulars')
#     else:
#         form = CircularForm()
#     return render(request, 'add_circular.html', {'form': form})

# def add_broadcast(request):
#     if request.method == 'POST':
#         form = BroadcastForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('broadcasts')
#     else:
#         form = BroadcastForm()
#     return render(request, 'add_broadcast.html', {'form': form})


def add_grievance(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            grievance = form.save(commit=False)
            if not grievance.user_name:  # If user name is not provided, default to anonymous
                grievance.user_name = 'Anonymous'
            grievance.save()
            return redirect('add_grievance')
    else:
        form = GrievanceForm()
    return render(request, 'add_grievance.html', {'form': form})


def add_suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            if not suggestion.user_name:  # If user name is not provided, default to anonymous
                suggestion.user_name = 'Anonymous'
            suggestion.save()
            return redirect('add_suggestion')
    else:
        form = SuggestionForm()
    return render(request, 'add_suggestion.html', {'form': form})


def calendar_view(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)

# def add_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('calendar_view')
#     else:
#         form = EventForm()
#     return render(request, 'add_event.html', {'form': form})
