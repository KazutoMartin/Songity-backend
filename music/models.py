from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    link = models.URLField(_("Link"), max_length=200)
    artist_id = models.CharField(_("ID"), max_length=50)
    uri = models.URLField(_("URI"), max_length=200)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    


class SpotifyAnalysis(models.Model):
    danceability = models.FloatField(_("danceability"))
    energy = models.FloatField(_("energy"))
    loudness = models.FloatField(_("loudness"))
    speechiness = models.FloatField(_("speechiness"))
    acousticness = models.FloatField(_("acousticness"))
    instrumentalness = models.FloatField(_("instrumentalness"))
    liveness = models.FloatField(_("liveness"))
    valence = models.FloatField(_("valence"))
    tempo = models.FloatField(_("tempo"))
    time_signature = models.FloatField(_("time_signature"))
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    

class Genre(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    similarity = models.FloatField(_("Similarity"))

class Song(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    album = models.CharField(_("Album"), max_length=50)
    artist = models.ManyToManyField(Artist, verbose_name=_("Artist"))
    song_id = models.CharField(_("ID"), max_length=50)
    link = models.URLField(_("Link"), max_length=200)
    image_link = models.URLField(_("Image Link"), max_length=200)
    preview_url = models.URLField(_("Preview URL"), max_length=200)
    uri = models.URLField(_("URI"), max_length=200)
    duration_ms = models.IntegerField(_("Duration(ms)"))
    spotify_analysis = models.ForeignKey(SpotifyAnalysis, verbose_name=_("spotify analysis"), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    first_genre = models.ForeignKey(Genre, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    second_genre = models.ForeignKey(Genre, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    third_genre = models.ForeignKey(Genre, verbose_name=_(""), on_delete=models.SET_NULL, null=True)
    
    

class PreviewListen(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    song = models.ForeignKey(Song, verbose_name=_("Song"), on_delete=models.CASCADE)
    count = models.IntegerField(_("Count"), default=0)
    
    
class SuggestedSongs(models.Model):
    songs = models.ManyToManyField(Song, verbose_name=_("Songs"))
    personality = models.ForeignKey("personality.Personality", verbose_name=_("Personality"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    
class LikeArtist(models.Model):
    artist = models.ForeignKey("music.Artist", verbose_name=_("Artist"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey('personality.Personality', verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)
    
class LikeSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey('personality.Personality', verbose_name=_("Personality"), on_delete=models.PROTECT)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)
    
class DislikeArtist(models.Model):
    artist = models.ForeignKey("music.Artist", verbose_name=_("Artist"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey('personality.Personality', verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    isliked_at = models.DateTimeField(_("Disliked at"), default=timezone.now)
    
class DislikeSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey('personality.Personality', verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    disliked_at = models.DateTimeField(_("Disliked at"), default=timezone.now)
    
class ShareSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey('personality.Personality', verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)
    

    
    
    
    

    
    