from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Image(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.name
