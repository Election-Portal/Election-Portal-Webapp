"""ElectionPortalWebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('province/', include('political_divisions.urls')),
    path('candidates/', include('candidates.urls')),
    path('parties/', include('political_parties.urls')),
    path('constituencies/', include('electoral_constituencies.urls')),
    path('blog/', include('blog.urls')),
    path('results/', include('results.urls')),
    path('', include('homepage.urls'), name = "HomePage"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', include('search.urls')),
    path('volunteers/', include('volunteers.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
