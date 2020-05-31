from django.urls import include, path
from . import views
urlpatterns = [
    path('get/', views.index, name="index"),
]
