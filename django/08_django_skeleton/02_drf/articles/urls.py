from django.urls import path
from . import views


urlpatterns = [
    path('aritlces/', views.article_list)
]
