from rest_framework import serializers
from .models import User, UserGroup

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class UserGroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = UserGroup
        fields = ['id', 'name', 'users']

class UserGroupAddUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True, help_text="The ID of the user to be added to the group.")
