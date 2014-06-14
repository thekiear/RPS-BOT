# myapp/api.py
from tastypie.resources import ModelResource
from match.models import Match, UserProfile, User, MatchRequest


class MatchRequestResource(ModelResource):
	class Meta:
		queryset = MatchRequest.objects.all()
		resource_name = 'matchRequest'

class MatchResource(ModelResource):
    class Meta:
        queryset = Match.objects.all()
        resource_name = 'match'

class UserProfileResource(ModelResource):
	class Meta:
		queryset = UserProfile.objects.all()
		resource_name = 'userProfile'

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'