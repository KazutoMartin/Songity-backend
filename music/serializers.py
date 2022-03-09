from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import DislikeSong, LikeSong, LikeArtist, DislikeArtist
from users.models import Profile

class LikeSongSerilizer(ModelSerializer):
    class Meta:
        model = LikeSong
        fields = '__all__'
    
class LikeArtistSerilizer(ModelSerializer):
    class Meta:
        model = LikeArtist
        fields = '__all__'
        

    class Meta:
        model = DislikeSong
        fields = ('id', )
        
        
class DislikeArtistSerilizer(ModelSerializer):
    class Meta:
        model = DislikeArtist
        fields = '__all__'

class DislikeSongSerilizer(ModelSerializer):
    class Meta:
        model = DislikeSong
        fields = '__all__'