from django.urls import path
from .views import *
urlpatterns = [
    path( 'result/<int:pk>', result.as_view(), name='result'),
    path('about', about.as_view(), name= 'about'),
    path('peek', peek.as_view(), name= 'peek'),
    path('', home.as_view(), name='home'),
]
