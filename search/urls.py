from django.conf.urls import url

from views import *

urlpatterns = [
    # url(r'^$', test, name='test'),
    url(r'^$', home, name='home'),
    url(r'^query$', query, name='query'),
]