from django.contrib import admin
from . import models
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.

class GenericOptionInline(NestedStackedInline):
    model = models.GenericOption
    extra = 1


class GenericParentOptionInline(NestedStackedInline):
    model = models.GenericParentOption
    extra = 0
    inlines = [GenericOptionInline]


class GenericFieldInline(NestedStackedInline):
    model = models.GenericField
    extra = 1
    inlines = [GenericParentOptionInline]


class GenericFormAdmin(NestedModelAdmin):
    inlines = [GenericFieldInline]


admin.site.register(models.GenericForm, GenericFormAdmin)


class GenericFieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.GenericField, GenericFieldAdmin)


class GenericParentOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.GenericParentOption, GenericParentOptionAdmin)


class GenericOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.GenericOption, GenericOptionAdmin)


class GenericFormDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.GenericFormData, GenericFormDataAdmin)
