from django.urls import path
from .views import GenreListView
from .views import GenreDetailView

urlpatterns = [
  path('', GenreListView.as_view()),
  path('<int:pk>', GenreDetailView.as_view()),
  ]