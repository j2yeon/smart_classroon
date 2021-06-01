from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path("my-info/", views.myInfo, name="my-info"),
    path("my-attendance/", views.myAttendance, name="my-attendance"),
    path("take_video/", views.takeVideo, name="take_video"),
    path("confirm-attendance/<int:lecture_id>/<int:weekNum>", views.confirmAttendance, name="confirm-attendance"),
    path("enrolment/",views.enrolment, name="enrolment"),
]
