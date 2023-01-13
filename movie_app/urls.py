from django.urls import path
from movie_app.views import movie_view, director_detail_view, director_view, review_view, movie_detail_view, \
    review_detail_view

urlpatterns = [
    path('directors/', director_view),
    path('directors/<int:id>/', director_detail_view),
    path('movies/', movie_view),
    path('movies/<int:id>/', movie_detail_view),
    path('reviews/', review_view),
    path('reviews/<int:id>/', review_detail_view),
]