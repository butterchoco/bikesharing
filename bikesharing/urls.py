"""bikesharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic.base import RedirectView
from rest_framework.authtoken.views import obtain_auth_token
from . import settings
from .utils.routers import router

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('admin/', admin.site.urls),
    path('router/', include(router.urls)),
    path('auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', include('home.urls', namespace='home')),
    path('user/', include('user.urls', namespace='registrasi')),
    path('transaction/', include('transaction.urls', namespace='transaction')),
    path('report/', include('report.urls', namespace='report')),
    path('acara/', include('acara.urls', namespace='acara')),
    path('penugasan/', include('penugasan.urls', namespace='penugasan')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
