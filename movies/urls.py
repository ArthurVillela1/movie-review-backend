from django.urls import path
from .views import MovieListView

urlpatterns = [
  path('', MovieListView.as_view()),
  path('<int:pk>/', MovieDetailView.as_view()),
]