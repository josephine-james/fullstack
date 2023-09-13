from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('event_details/<int:pk>', views.detail, name='detail')
    ]