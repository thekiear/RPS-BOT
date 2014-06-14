from django.conf.urls import patterns, include, url
from django.contrib import admin
from match.api import MatchResource, UserProfileResource, UserResource, MatchRequestResource
from tastypie.api import Api
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserProfileResource())
v1_api.register(MatchResource())
v1_api.register(UserResource())
v1_api.register(MatchRequestResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'referee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^player/', 'player.views.home', name='player_app_home'),
    url(r'^match/', 'match.views.home_page', name="match_home"),
    url(r'^matchRequest/', 'match.views.join_match', name="join_match"),
    url(r'^register/$','match.views.register', name='register'),
    url(r'^$', 'match.views.register', name="root_page"),
    url(r'^api/', include(v1_api.urls)),
)
