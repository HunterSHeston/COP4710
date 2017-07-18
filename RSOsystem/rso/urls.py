from django.conf.urls import url
from . import views

# name space for urls allow us to distinguish between to urls named index or detail
app_name = 'rso'

# regular expression numbers examples
# url(r'^(?P<varName>[0-9]+[0-9]+[0-9])/$'), views.someView, 'someName')
# this would recognize a url with three digits 0 to 9 or an int from 0 to 999
# the number will be stored in "varName" and can(and should) be passed to the view.someView method
# ex) def someView(request, varName):    // this will allow you to use the value requested when handling the url



urlpatterns = [
    # /rso/
    url(r'^$', views.index, name='index'),
    # /rso/24
    # url(r'^(?P<uID>[0-9]+)/$', views.detail, name='detail'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^map/$', views.map, name='map'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^joinRso/$', views.joinRso, name='joinRso'),
    url(r'^(?P<rsoID>[0-9]+)/$', views.add, name='add'),
    url(r'^createRso/$', views.createRso, name='createRso'),

]
