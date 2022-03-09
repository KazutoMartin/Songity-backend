from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from personality.serializers import PersonalitySerializer
from users.serializers import ProfileSerializer, UserSerilizer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_personality(request):
    serializer = PersonalitySerializer(data=request.data)
    if serializer.is_valid():
        p = serializer.create(serializer.validated_data)
        p.save()
        profile = request.user.profile
        profile.current_personality = p
        profile.search_history.add(p)
        profile.save()
        return Response({
            'code':200,
            'object':PersonalitySerializer(p).data,
            'user':UserSerilizer(request.user).data,
            'profile':ProfileSerializer(profile).data
            
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'code':406,
            'error': serializer.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
    
