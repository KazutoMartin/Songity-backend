from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from users.models import Profile

class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')
        read_only_fields = ('is_staff','id')
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validate_data):
        return User(**validate_data)
    
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username', 'age','user' )
        read_only_fields = ('user','id')
