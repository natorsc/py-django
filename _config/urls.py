"""
URL configuration for _config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # Apps.
    path("accounts/", include("accounts.urls")),
    path("", include("task.urls")),
]

if settings.DEBUG:
    # 1. Ativa as rotas internas para servir arquivos estáticos globais
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # 2. Ativa as rotas internas para servir mídias de upload (ex: fotos de perfil)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # 3. Injeta as rotas do Django Debug Toolbar se ele estiver carregado
    if "debug_toolbar" in settings.INSTALLED_APPS:
        urlpatterns += [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
