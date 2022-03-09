from django.urls import path

from .views import like_song, like_artist, undo_dislike_artist, undo_dislike_song, undo_like_artist, undo_like_song


urlpatterns = [
    path('like-song/', like_song),
    path('like-artist/', like_artist),
    path('undo-like-artist/', undo_like_artist),
    path('undo-like-song/', undo_like_song),
    path('undo-dislike-song/', undo_dislike_song),
    path('undo-dislike-artist/', undo_dislike_artist),
    
    
]