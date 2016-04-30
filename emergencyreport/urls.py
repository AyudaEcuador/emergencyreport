from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'emergencyreport.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-forms/', include('genericform.urls')),
    url(r'^reporte/', TemplateView.as_view(template_name='djform.html')),
]
