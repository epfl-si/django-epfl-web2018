"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app.views import error_400, error_403, error_500, message_warning
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
    path("admin/", admin.site.urls),
    path("400/", error_400, name="error_400"),
    path("403/", error_403, name="error_403"),
    path("500/", error_500, name="error_500"),
    path("warning/", message_warning, name="warning"),
]

handler400 = "django_epfl_web2018.views.error_400"
handler403 = "django_epfl_web2018.views.error_403"
handler404 = "django_epfl_web2018.views.error_404"
handler500 = "django_epfl_web2018.views.error_500"
