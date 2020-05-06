from djoser import serializers as djoser_serializers
from accounts.models import User


class UserMeSerializer(djoser_serializers.UserSerializer):

    class Meta:
        model = User
        fields = ('username', 'role', 'id', 'auth_token', 'admins_services', 'organisation')
