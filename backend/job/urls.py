from django.urls import path

from .views import JobListView

app_name = 'job'
urlpatterns = [
    path('', JobListView.as_view()),
]
