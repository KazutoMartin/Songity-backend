from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator



class Personality(models.Model):
    mind = models.CharField(_("Mind"), max_length=1)
    mind_p = models.IntegerField(_("Mind percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True)
    energy = models.CharField(_("Energy"), max_length=1)
    energy_p = models.IntegerField(_("Energy percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True)
    nature = models.CharField(_("Nature"), max_length=1)
    nature_p = models.IntegerField(_("Nature percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True)
    tactics = models.CharField(_("Tactics"), max_length=1)
    tactics_p = models.IntegerField(_("Tactics percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    
    
    
class LikeArtist(models.Model):
    artist = models.ForeignKey("music.Artist", verbose_name=_("Artist"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)
    
class LikeSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)
    
class DislikeArtist(models.Model):
    artist = models.ForeignKey("music.Artist", verbose_name=_("Artist"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    disliked_at = models.DateTimeField(_("Disliked at"), default=timezone.now)
    
class DislikeSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    disliked_at = models.DateTimeField(_("Disliked at"), default=timezone.now)
    
class ShareSong(models.Model):
    song = models.ForeignKey("music.Song", verbose_name=_("Song"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    personality = models.ForeignKey(Personality, verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True)
    liked_at = models.DateTimeField(_("Liked at"), default=timezone.now)