
from django.contrib import admin
from example.models import Example, ExampleCategory
from example.forms import ExampleAdminForm

class ExampleAdmin(admin.ModelAdmin):
    list_editable = ('is_active', )
    list_display = ('id', 'title', 'is_active', 'image', 'category',)
    form = ExampleAdminForm

admin.site.register(Example, ExampleAdmin)


class ExampleCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExampleCategory, ExampleCategoryAdmin)