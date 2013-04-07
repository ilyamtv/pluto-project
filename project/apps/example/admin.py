
from django.contrib import admin
from example.models import Example

class ExampleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Example, ExampleAdmin)