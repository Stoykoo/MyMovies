from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.custom_login, name='custom_login'),
    path("<int:movie_id>/", views.movie_detail, name="movie_detail"),
    path('logout/', views.logout_view, name='logout'),
    ]