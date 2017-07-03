from django.conf.urls import url

from . import views


# regular expression numbers examples
# url(r'^(?P<varName>[0-9]+[0-9]+[0-9])/$'), views.someView, 'someName')
# this would recognize a url with three digits 0 to 9 or an int from 0 to 999
# the number will be stored in "varName" and can(and should) be passed to the view.someView method
# ex) def someView(request, varName):    // this will allow you to use the value requested when handling the url


urlpatterns = [
    # /rso/
    url(r'^$', views.index, name='index'),

    # /rso/24
    url(r'^(?P<rso_id>[0-9]{1})/$', views.details, name='details'),

]