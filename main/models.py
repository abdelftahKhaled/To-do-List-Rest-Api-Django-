from django.db import models
from django.utils.translation import gettext_lazy as _

from helper.models import Trickingmodel
from authantiction.models import User
class todo(Trickingmodel,models.Model):
    owner=models.ForeignKey(to=User, verbose_name=_(""), on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    desc =models.TextField(_("desc"),max_length=150)
    is_complete =models.BooleanField(_("is_complet"),default=False)
    def __str__(self):
        return self.title