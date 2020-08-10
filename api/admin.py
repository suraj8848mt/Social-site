from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    Item, 
    Comment, 
    Like, 
    Asset, 
    AssetBundle, 
    Profile)


class ItemAdmin(admin.ModelAdmin):
    list_display = [ 'owner', 'asset_bundle', 'created_at']

    search_fields = ['title']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

    search_fields= ['user']

class CommentAdmin(admin.ModelAdmin):
    list_display= ['owner', 'created_at']


class LikeAdmin(admin.ModelAdmin):
    list_display= ['owner', 'item', 'created_at']

class AssetBundleAdmin(admin.ModelAdmin):
    list_display = ['salt', 'kind', 'owner']

class AssetAdmin(admin.ModelAdmin):

    def preview(self, obj):
        return mark_safe('<image src="%s" width="100" />' % obj.full_url)

    preview.allow_tags=True

    list_display = ['preview', 'kind', 'extension', 'full_url']



admin.site.register(Item, ItemAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetBundle, AssetBundleAdmin)
