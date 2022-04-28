from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from users.serializers import ProfileSerializer
from users.serializers import UserSerilizer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


from users.mixins import ApiErrorsMixin, PublicApiMixin


# from users.selectors import user_get_me
from users.services import google_validate_id_token, google_get_user_info


class UserInitApi(PublicApiMixin, ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        googleId = serializers.IntegerField()
        profile_pic = serializers.URLField(required=False, default="")
        accessToken = serializers.CharField()
        
    def post(self, request, *args, **kwargs):
        id_token = request.data['data']['id_token']
        # print(id_token)
        google_validate_id_token(id_token=id_token)
        
        serializer = self.InputSerializer(data=request.data['data'])
        if serializer.is_valid():
            access_token = serializer.validated_data.get('accessToken')
            google_info = google_get_user_info(access_token=access_token)
            print(google_info)
            googleId = str(serializer.validated_data.get('googleId'))
            if google_info['sub'] != googleId:
                return Response({'code':400, 'errors':'Access Token didnt match with Google ID'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = User.objects.get(username=googleId)
            except User.DoesNotExist:
                first_name = serializer.validated_data.get('first_name')
                last_name = serializer.validated_data.get('last_name')
                
                user = User.objects.create(username=googleId, first_name=first_name, last_name=last_name)
                user.profile.email = serializer.validated_data.get('email')
                user.profile.google_profile_url = serializer.validated_data.get('profile_pic')
                user.profile.save()
            
            token = Token.objects.get_or_create(user=user)
            print(token[0])
            print(token[0].key)
            
            

            return Response({'code':200, 'user':UserSerilizer(user).data, 'profile':ProfileSerializer(user.profile).data, 'token':token[0].key}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({'code':400, 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_user(request):
    print(request.user)
    if request.user.is_authenticated:
        user = request.user 
        print('hey')
        print(user)
        return Response({"code":200, "user":{'user':UserSerilizer(user).data, 'profile':ProfileSerializer(user.profile).data}})
    else:
        print('no hery')
        return Response({"code":200, "user":False})
