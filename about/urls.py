from .templates.about import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
]
