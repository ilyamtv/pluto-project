
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Example(models.Model):

    class Meta:
        db_table = 'example'
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
        ordering = ['-pk']


    title = models.CharField(null=False, max_length=255, verbose_name=_('Title'))

    def __unicode__(self):
        return self.title