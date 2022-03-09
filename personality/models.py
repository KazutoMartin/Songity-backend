from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator



class Personality(models.Model):
    e = [
        ('E', _('EXTRAVERTED')),
        ('I', _('INTROVERTED')),
    ]
    n = [
        ('N', _('INTUITIVE')),
        ('S', _('OBSERVANT')),
    ]
    f = [
        ('F', _('FEELING')),
        ('T', _('THINKING')),
    ]
    j = [
        ('J', _('JUDGING')),
        ('P', _('Email')),
    ]
    
    mind = models.CharField(_("Mind"), max_length=1, choices=e)
    mind_p = models.IntegerField(_("Mind percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True, blank=True)
    energy = models.CharField(_("Energy"), max_length=1, choices=n)
    energy_p = models.IntegerField(_("Energy percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True, blank=True)
    nature = models.CharField(_("Nature"), max_length=1, choices=f)
    nature_p = models.IntegerField(_("Nature percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True, blank=True)
    tactics = models.CharField(_("Tactics"), max_length=1, choices=j)
    tactics_p = models.IntegerField(_("Tactics percentage"), validators=[MinLengthValidator(1), MaxLengthValidator(100)], null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)