
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Example(models.Model):

    class Meta:
        db_table = 'example'
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
        ordering = ['-pk']

    title = models.CharField(null=False, max_length=255, verbose_name=_('Title'))
    category = models.ForeignKey('example.ExampleCategory', null=True, blank=True)
    image = models.ImageField(upload_to='example', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date_state = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.title


class ExampleCategory(models.Model):

    class Meta:
        db_table = 'example_category'
        verbose_name = _('Example category')
        verbose_name_plural = _('Example categories')

    name = models.CharField(null=False, max_length=64, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name