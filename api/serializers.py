from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Item


class UserSerializer(serializers.ModelSerializer):
    """
    User Detail Serializer 
    """

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
        read_only_field = ('id',)


# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=255)
#     subtitle = serializers.CharField(required=False, allow_blank=True, max_length=255)
#     owner_id = serializers.IntegerField(required=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Item.objects.create(**validated_data)

class ItemSerializer(serializers.ModelSerializer):
    """
    Item Detail Serializers
    """

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'subtitle',
            'owner',
        )
        read_only_fields = ('id',)

class ItemDetailSerializers(serializers.ModelSerializer):

    """
    Item Detail Serializers
    """

    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'subtitle',
            'owner',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('id',)