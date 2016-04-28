from django.contrib import admin
from genericform.models import GenericForm, GenericField, GenericParentOption, GenericOption
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


# Register your models here.

class GenericOptionInline(NestedStackedInline):
    model = GenericOption
    extra = 1


class GenericParentOptionInline(NestedStackedInline):
    model = GenericParentOption
    extra = 0
    inlines = [GenericOptionInline]


class GenericFieldInline(NestedStackedInline):
    model = GenericField
    extra = 1
    inlines = [GenericParentOptionInline]


class GenericFormAdmin(NestedModelAdmin):
    inlines = [GenericFieldInline]


admin.site.register(GenericForm, GenericFormAdmin)


class GenericFieldAdmin(admin.ModelAdmin):
    pass


admin.site.register(GenericField, GenericFieldAdmin)


class GenericParentOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(GenericParentOption, GenericParentOptionAdmin)


class GenericOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(GenericOption, GenericOptionAdmin)
