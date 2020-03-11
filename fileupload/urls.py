from django.conf.urls import url
from . import views

urlpatterns = [
    url('files/', views.FileUploadView.as_view(),name='fileupload'),
    url('file/(?P<id>[0-9]+)/$',views.GetFile.as_view())

]
