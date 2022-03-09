from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    ways = [
        ('TL', _('Telegram')),
        ('EM', _('Email')),
        ('SM', _('SMS')),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(_("Username"), max_length=50, unique=True, null=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True, null=True)
    google_profile_url = models.URLField(_("Google Profile URL"), max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    age = models.IntegerField(_("Age"), null=True)
    last_modified = models.DateTimeField(_('last modified'),auto_now=True)
    
    liked_songs = models.ManyToManyField("music.Song", verbose_name=_("Liked Songs"))
    liked_artists = models.ManyToManyField("music.Artist", verbose_name=_("Liked Artists"))
    
    current_personality = models.ForeignKey("personality.Personality", verbose_name=_("Personality"), on_delete=models.SET_NULL, null=True,
                                    related_name='main_persoanlity')
    search_history = models.ManyToManyField("personality.Personality", verbose_name=_("Personality History"), related_name='persoanlity_history')
    
    suggested_songs = models.ManyToManyField("music.SuggestedSongs", verbose_name=_("Suggested Songs"))
    def __str__(self):
        return self.user.username



###################### Signals for Profile model #######################
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
#######################################################