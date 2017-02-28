from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^', views.game_list, name='gameList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)