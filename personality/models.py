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