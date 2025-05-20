# celebration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('relay/', views.relay, name='relay'),
    path('relay/count/', views.relay_count, name='relay_count'),
    path('bless/send/', views.bless_send, name='bless_send'),
    path('bless/list/', views.bless_list, name='bless_list'),
]
