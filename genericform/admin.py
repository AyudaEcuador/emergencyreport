from django.contrib import admin
from genericform.models import GenericForm, GenericField
# Register your models here.

class GenericFormAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericForm,GenericFormAdmin)

class GenericFieldAdmin(admin.ModelAdmin):
    pass
admin.site.register(GenericField,GenericFieldAdmin)