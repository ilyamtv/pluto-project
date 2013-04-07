
from django.contrib import admin
from example.models import Example, ExampleCategory

class ExampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Example, ExampleAdmin)


class ExampleCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExampleCategory, ExampleCategoryAdmin)