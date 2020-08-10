from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import AssetBundle
from api.serializers.user import UserSerializer



class AssetBundleSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = AssetBundle
        fields = (
            'id',
            'salt',
            'owner',
            'kind',
            'base_url',
            'owner',
            'created_at',

        )
        read_only_fields = ('id',)


class AssetBundleDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = AssetBundle
        fields =(
            'id',
            'salt',
            'owner',
            'kind',
            'asset_urls',
            'base_url',
            'owner',
            'created_at',
            

        )
        read_only_fields = ('id',)
