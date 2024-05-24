from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path("your_name/", views.get_name, name="get_name"),
        path('logout/', views.logout_view, name='logout'),
    ]