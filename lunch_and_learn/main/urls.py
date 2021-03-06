from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("create_event", views.create_event, name="create_event"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("choose_skill", views.choose_skill, name="choose_skill"),
    path("choose_lead", views.choose_lead, name="choose_lead"),
    path("choose_time", views.choose_time, name="choose_time"),
    path("submit", views.submit, name="submit")
]