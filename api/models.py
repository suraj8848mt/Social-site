from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):

    """ This is model for items """

    title = models.CharField(max_length=255)
    subtitle = models.CharField( max_length=50, blank=True, null=True)
    like_count = models.IntegerField(default=0)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    @property
    def full_title(self):
        if self.subtitle:
            return "%s | %s" % (self.title, self.subtitle)
        return self.title
    
    @property
    def owner_email(self):
        return self.owner.email

    def __str__(self):
        return self.title