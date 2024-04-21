from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    # path('grievances/', views.grievances_view, name='grievances_view'),
    path('add/', views.add_grievance, name='add_grievance'),
    # path('suggestions/', views.suggestions_view, name='suggestions_view'),
    path('suggestions/add/', views.add_suggestion, name='add_suggestion'),
    # path('add_event/', views.add_event, name='add_event'),
    path('announcements/', views.announcements_view, name='announcements'),
    path('circulars/', views.circulars_view, name='circulars'),
    path('broadcasts/', views.broadcasts_view, name='broadcasts'),
    #     path('announcements/add/', views.add_announcement, name='add_announcement'),
    #     path('circulars/add/', views.add_circular, name='add_circular'),
    #     path('broadcasts/add/', views.add_broadcast, name='add_broadcast'),
    path('clubs/', views.clubs_page, name='clubs'),
    path('contribute/', views.contribute, name='contribute'),
    path('contribute/success/', views.contribute_success,
         name='contribute_success'),
    path('gallery/', views.gallery , name='gallery'),
]
