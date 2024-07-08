from django.urls import path
from .views import DirectorListView
from .views import DirectorDetailView

urlpatterns = [
  path('', DirectorListView.as_view()),
  path('<int:pk>', DirectorDetailView.as_view()),
  ]