from django.conf.urls import url, include
from . import views
urlpatterns = [

    url(r'^$', views.index, name = 'main'),
    url(r'^$logged_in', views.logged_in, name = 'logged_in'),
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
    url(r'^free_notice', views.add_free_notice, name = 'add_free_notice'),
    url(r'^free_board', views.free_notice, name = 'free_notice'),
    url(r'^tosubmitpost', views.tosubmitpost, name = 'tosubmitpost'),
    url(r'^(?P<pk>\d+)/$', views.postdetail, name = 'postdetail'),
    url(r'^(?P<pk>\d+)/comment/new/$', views.comment_new),
    
]
