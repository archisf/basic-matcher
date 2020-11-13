from django.urls import path

from .views import CandidateFinderView

app_name = 'candidate'
urlpatterns = [
    path('search/', CandidateFinderView.as_view(), name='search'),
]
