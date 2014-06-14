from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tastypie.utils.timezone import now

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    callback_url = models.URLField(blank=True)
    
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Match(models.Model):
    players = models.ManyToManyField(User)
   # player2 = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.body

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.body)[:50]

        return super(Entry, self).save(*args, **kwargs)

class MatchRequest(models.Model):
    player = models.OneToOneField(UserProfile)
    pub_date = models.DateTimeField(default=now)

    def __unicode__(self):
        return "this is a matcherequest"