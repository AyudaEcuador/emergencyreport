from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from accounts.views import my_logout
urlpatterns = [
    # Examples:
    url(r'^$', 'shell.views.landing', name='landing'),
    url(r'^login/', 'accounts.views.login', name='login'),

    url(r'^mesa/(?P<mesa_id>\d+)/reportes/$', 'genericform.views.formularios_por_mesa', name='formularios_por_mesa'),

    url(r'^mesas/$', 'genericform.views.mesas', name='mesas'),

    # url(r'^login/', include(admin.site.urls)),



    url(r'^logout/$', my_logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-forms/', include('genericform.urls')),
    url(r'^reporte/', TemplateView.as_view(template_name='djform.html')),


    url(r'^mesa/(?P<mesa_id>\d+)/reporte/(?P<reporte_id>\d+)$', TemplateView.as_view(template_name='djform.html')),

]
