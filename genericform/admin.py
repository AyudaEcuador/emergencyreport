from django.contrib import admin
from genericform.models import GenericForm, GenericField, GenericParentOption, GenericOption

# Register your models here.

class GenericFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericForm,GenericFormAdmin)

class GenericFieldAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericField,GenericFieldAdmin)

class GenericParentOptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericParentOption,GenericParentOptionAdmin)

class GenericOptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericOption,GenericOptionAdmin)


