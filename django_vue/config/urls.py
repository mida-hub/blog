"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog-auth/', obtain_jwt_token),
    path('blog-api/', include('blog.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='blog'),
    path('posts/', TemplateView.as_view(template_name='index.html'), name='blog'),
    path('posts/<int:pk>/', TemplateView.as_view(template_name='index.html'), name='blog'),
    path('posts/tags/', TemplateView.as_view(template_name='index.html'), name='blog'),
    path('posts/tags/<int>/', TemplateView.as_view(template_name='index.html'), name='blog'),
    path('auth/', TemplateView.as_view(template_name='index.html'), name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
