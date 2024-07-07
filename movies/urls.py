from django.urls import path
from .views import MovieListView
from .views import MovieDetailView

urlpatterns = [
  path('', MovieListView.as_view()),
  path('<int:pk>', MovieDetailView.as_view()),
]