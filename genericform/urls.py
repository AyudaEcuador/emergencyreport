from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^metadata/(?P<pk>\w+)', views.FormMetadataView.as_view())
]