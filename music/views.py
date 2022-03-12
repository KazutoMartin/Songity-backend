from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes

from .models import LikeSong, LikeArtist, DislikeSong, DislikeArtist
from .serializers import DislikeSongSerilizer, LikeArtistSerilizer, LikeSongSerilizer, DislikeArtistSerilizer
from rest_framework.permissions import IsAuthenticated

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
user_response = openapi.Response('response description', LikeSongSerilizer)



# @swagger_auto_schema(method='get', manual_parameters=[test_param], responses={200: user_response})
@swagger_auto_schema(methods=['post'], request_body=LikeSongSerilizer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_song(request):
    print(request.user)
    serializer = LikeSongSerilizer(data=request.data)
    if serializer.is_valid():
        song = serializer.validated_data['song']
        per = serializer.validated_data['personality']
        try:
            LikeSong.objects.get(user=request.user, song=song, personality=per)
            return Response({
                'code':400,
                'response':'already liked',
            }, status=status.HTTP_400_BAD_REQUEST)
        except LikeSong.DoesNotExist:
            object = LikeSong(user=request.user, personality=per, song=song)
            object.save()
            return Response({
                'code':200,
                'object':LikeSongSerilizer(object).data,
            }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'code':406,
            'error': serializer.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
@swagger_auto_schema(methods=['post'], request_body=LikeArtistSerilizer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_artist(request):
    print(request.user)
    serializer = LikeArtistSerilizer(data=request.data)
    if serializer.is_valid():
        artist = serializer.validated_data['artist']
        per = serializer.validated_data['personality']
        try:
            LikeArtist.objects.get(user=request.user, artist=artist, personality=per)
            return Response({
                'code':400,
                'response':'already liked',
            }, status=status.HTTP_400_BAD_REQUEST)
        except LikeArtist.DoesNotExist:
            object = LikeArtist(user=request.user, personality=per, artist=artist)
            object.save()
            return Response({
                'code':200,
                'object':LikeArtistSerilizer(object).data,
            }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'code':406,
            'error': serializer.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
@swagger_auto_schema(methods=['post'], request_body=DislikeArtistSerilizer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_artist(request):
    print(request.user)
    serializer = DislikeArtistSerilizer(data=request.data)
    if serializer.is_valid():
        artist = serializer.validated_data['artist']
        per = serializer.validated_data['personality']
        try:
            DislikeArtist.objects.get(user=request.user, artist=artist, personality=per)
            return Response({
                'code':400,
                'response':'already Disliked',
            }, status=status.HTTP_400_BAD_REQUEST)
        except DislikeArtist.DoesNotExist:
            object = DislikeArtist(user=request.user, personality=per, artist=artist)
            object.save()
            return Response({
                'code':200,
                'object':DislikeArtistSerilizer(object).data,
            }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'code':406,
            'error': serializer.errors
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
 
 
@swagger_auto_schema(methods=['delete'], request_body=LikeSongSerilizer)       
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def undo_like_song(request):
    id = request.data['id']
    object = get_object_or_404(LikeSong, pk=id, user=request.user)
    print(object.id)
    serialized_object = LikeSongSerilizer(object).data
    object.delete()
    return Response({
        'code':200,
        'object': serialized_object,
        'response':'deleted'
    }, status=status.HTTP_200_OK)
    

@swagger_auto_schema(methods=['delete'], request_body=LikeArtistSerilizer)       
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def undo_like_artist(request):
    id = request.data['id']
    object = get_object_or_404(LikeArtist, pk=id, user=request.user)
    print(object.id)
    serialized_object = LikeArtistSerilizer(object).data
    object.delete()
    return Response({
        'code':200,
        'object': serialized_object,
        'response':'deleted'
    }, status=status.HTTP_200_OK)
  
  
@swagger_auto_schema(methods=['delete'], request_body=DislikeSongSerilizer)             
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def undo_dislike_song(request):
    id = request.data['id']
    object = get_object_or_404(DislikeSong, pk=id, user=request.user)
    print(object.id)
    serialized_object = DislikeSongSerilizer(object).data
    object.delete()
    return Response({
        'code':200,
        'object': serialized_object,
        'response':'deleted'
    }, status=status.HTTP_200_OK)
        
        
@swagger_auto_schema(methods=['delete'], request_body=DislikeArtistSerilizer)             
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def undo_dislike_artist(request):
    id = request.data['id']
    object = get_object_or_404(DislikeArtist, pk=id, user=request.user)
    print(object.id)
    serialized_object = DislikeArtistSerilizer(object).data
    object.delete()
    return Response({
        'code':200,
        'object': serialized_object,
        'response':'deleted'
    }, status=status.HTTP_200_OK)
        