
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pluto.utils.upload import beauty_upload_to

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


class ExampleImage(models.Model):

    def _upload_to(instance, filename):
        return beauty_upload_to('example/%s' % str(instance.example_id), filename)

    class Meta:
        db_table = 'example_images'
        verbose_name = _('Example category')
        verbose_name_plural = _('Example categories')

    example = models.ForeignKey('example.Example', null=False)
    image = models.ImageField(upload_to=_upload_to, null=False)
    title = models.CharField(null=False, max_length=255, verbose_name=_('Title'))
    sort = models.IntegerField(null=False, default=0, verbose_name=_('Sort'))


    def __unicode__(self):
        return "%s" % str(self.pk)

    def save(self, *args, **kwargs):
        if not self.pk:
            max_sort = self.__class__.objects.filter(example=self.example).aggregate(m=models.Max('sort'))['m'] or 0
            self.sort = max_sort + 1

        super(ExampleImage, self).save(*args, **kwargs)