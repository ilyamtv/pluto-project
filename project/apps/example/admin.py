
from django.contrib import admin
from example.models import Example, ExampleCategory, ExampleImage
from example.forms import ExampleAdminForm


class ExampleImageInline(admin.TabularInline):
    model = ExampleImage
    extra = 0


class ExampleAdmin(admin.ModelAdmin):

    list_editable = ('is_active', )
    list_display = ('id', 'title', 'is_active', 'image', 'category',)
    list_per_page = 30
    list_filter = ('category', 'is_active',)
    search_fields = ['title']

    form = ExampleAdminForm
    save_on_top = False
    readonly_fields = ()

    inlines = [ExampleImageInline]

admin.site.register(Example, ExampleAdmin)


class ExampleCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExampleCategory, ExampleCategoryAdmin)

