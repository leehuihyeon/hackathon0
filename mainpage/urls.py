from django.conf.urls import url, include
from . import views
urlpatterns = [

    url(r'^$', views.index, name = 'index'),
    url(r'^sogae', views.sogae, name = 'sogae'),
    url(r'^notice', views.notice, name = 'notice'),
    url(r'^ranking', views.raking, name = 'ranking'),
    url(r'^uni_list', views.uni_list, name = 'uni_list'),
    url(r'^add_song', views.add_song, name = 'add_song'),
    url(r'^mysong', views.mysong, name = 'mysong'),
    url(r'^event', views.event, name = 'event'),
    url(r'^signup', views.Signup, name = 'signup'),
    url(r'^signin', views.Signin, name = 'signin'),
    url(r'^logged', views.logged_in, name = 'logged'),
  
]
