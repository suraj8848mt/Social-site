from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Profile(models.Model):
    """
    User Profile Models
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    website_url = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        self.user.username


class AssetBundle(models.Model):
    """
     Asset bundle profile model
    {hbase_url}/{ab_kind}/{ab_salt}_{a_kind}.{a_extension}/
     https://res.cloudinary.com/upload/{ab_kind}/{ab_salt}_{a_kind}.{a_extension}/
    """
    KIND_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video')
    )


    salt = models.CharField(max_length=16)
    kind = models.CharField(max_length=5, choices=KIND_CHOICES, default="image")
    base_url = models.CharField(max_length=255, default=settings.S3_BASE_URL)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    def __str__(self):
        return "AssetBundle: %s" % self.salt
    
    def asset_urls(self): 
        array = []
        for asset in Asset.objects.filter(asset_bundle=self):
            array.append({asset.kind: asset.full_url})
        
        return array




class Asset(models.Model):
    """
    Asset Model
    """
    KIND_CHOICES = (
        ('original', 'Original'),
        ('large', 'Large'),
        ('small', 'Small')
    )

    EXTENSION_CHOICES = (
        ('png', 'png'),
        ('gif', 'gif'),
        ('jpg', 'jpg'),
        ('jpeg', 'jpeg'),
    )

    asset_bundle = models.ForeignKey(AssetBundle, on_delete=models.CASCADE)
    kind = models.CharField(max_length=8, choices=KIND_CHOICES, default="original")
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    extension = models.CharField(max_length=4, choices=EXTENSION_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)


    def __str__(self):
       return "Asset: %s: %s" % (self.asset_bundle.salt, self.kind)

    @property
    def full_url(self):
        return "%s%s/%s_%s.%s" % (self.asset_bundle.base_url, self.asset_bundle.kind, self.asset_bundle.salt, self.kind, self.extension)
            #  {base_url}{ab_kind}/{ab_salt}_{a_kind}.{a.extension}

            
class Item(models.Model):

    """ This is model for items """

    asset_bundle = models.ForeignKey(AssetBundle, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)


    def __str__(self):
        return "Item: %s: %s" % (self.owner.username, self.asset_bundle)



class Comment(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    body = models.TextField()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)

    