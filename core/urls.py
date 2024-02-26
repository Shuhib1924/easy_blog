"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings

from blogs import views as BlogView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("blogs.urls")),
    path("blog/<slug:slug>/", BlogView.blogs, name="blogs"),
    path("blog/search", BlogView.search, name="search"),
    path("register", BlogView.register, name="register"),
    path("login", BlogView.login, name="login"),
    path("logout", BlogView.logout, name="logout"),
    path("dashboard/", include("dashboards.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
