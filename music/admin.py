from django.contrib import admin
from .models import Artist, Song, LikeArtist, LikeSong

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(LikeArtist)
admin.site.register(LikeSong)



