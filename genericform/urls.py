from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^metadata/(?P<pk>\w+)', views.FormMetadataView.as_view()),
    url(r'^forms/(?P<form>\w+)', views.FormDataView.as_view()),
]
