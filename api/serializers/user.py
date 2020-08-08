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
