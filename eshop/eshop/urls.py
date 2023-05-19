"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from product.views import home, search
from account.views import log_in, register, log_out
from django.conf.urls.static import static, settings
from .api import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('search/', search, name='search'),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
