from django import forms
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class AdminImageWidget(forms.ClearableFileInput):

    template_with_image = '<p class="image-upload">%s</p>'
    template_image = '<a href="%s" target="_blank" class="image-original"><img src="%s" /></a> <br/>'
    template_with_clear = ('<span class="clearable-file-input">%s</span>' % forms.ClearableFileInput.template_with_clear)

    def __init__(self, *args, **kwargs):

        self.url_length = kwargs.pop('url_length', 30)
        self.preview = kwargs.pop('preview', False)
        self.crop = kwargs.pop('crop', None)
        self.image_size = kwargs.pop('image_size', "200x200")

        super(AdminImageWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        output = [super(AdminImageWidget, self).render(name, value, attrs)]

        if value and hasattr(value, "url"):
            image = get_thumbnail(value.path, self.image_size, crop=self.crop)
            output.insert(0, self.template_image % (value.url, image.url))

        return mark_safe(self.template_with_image % " ".join(output))