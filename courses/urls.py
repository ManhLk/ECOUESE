from django.urls import path, include, re_path
from courses.views import index

urlpatterns = [
    path('', index),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]