from django.conf.urls import url

from . import views

handler404 = 'tournament.views.handler404'

urlpatterns = [
    url(r'^index/', views.index, name='index'),  # Main site, where all news and images will be displayed
    url(r'^registration/', views.registration, name='registration'),
    url(r'^registration/', views.get_school_code, name='schoolcode'),
]
