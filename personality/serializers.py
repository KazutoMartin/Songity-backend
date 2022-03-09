from rest_framework.serializers import ModelSerializer, Serializer

from personality.models import Personality

class PersonalitySerializer(ModelSerializer):
    class Meta:
        model = Personality
        fields = '__all__'
        
    def create(self, validate_data):
        return Personality(**validate_data)
