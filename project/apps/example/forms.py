from django import forms
from example.models import Example, ExampleCategory
from pluto.admin.widgets import AdminImageWidget

class ExampleAdminForm(forms.ModelForm):

    class Meta:
        model = Example
        widgets = {
            'image': AdminImageWidget(image_size='100x100')
        }