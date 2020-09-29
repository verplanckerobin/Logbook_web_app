from django.urls import path
from . import views

app_name = "logbook"

urlpatterns = [
    path("", views.logbook_overview, name="logbook_overview"),
    path("<int:logbook_id>", views.logbook_details, name="logbook_details"),
    path('more/', views.more, name="logbook_more"),
    path('aircraft/', views.aircraft, name="aircraft"),
    path('airports/', views.airports, name="airports"),
    path('people/', views.people, name="people"),
    path('add_aircraft/', views.add_aircraft, name="add_aircraft"),
    path('add_airport/', views.add_airport, name="add_airport"),
    path('add_people/', views.add_people, name="add_people"),
    path('add_log/', views.add_log, name="add_log"),
    path('edit_log/<str:pk>', views.edit_log, name="edit_log"),
    path('edit_aircraft/<str:pk>', views.edit_aircraft, name="edit_aircraft"),
    path('edit_airport/<str:pk>', views.edit_airport, name="edit_airport"),
    path('edit_people/<str:pk>', views.edit_people, name="edit_people"),
]
