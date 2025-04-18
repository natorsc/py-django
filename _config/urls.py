"""
URL configuration for _config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.sitemaps import views as sitemaps_views
from django.urls import include, path
from django.views.i18n import JavaScriptCatalog

from home.sitemaps import HomeSitemap

apps_sitemap = {
    'home': HomeSitemap,
}

urlpatterns = [
    ## Django.
    path('admin/', admin.site.urls),
    path(route='accounts/', view=include('django.contrib.auth.urls')),
    ## I18n.
    path(route='i18n/', view=include('django.conf.urls.i18n')),
    path(
        route='jsi18n/',
        view=JavaScriptCatalog.as_view(),
        name='javascript-catalog',
    ),
    path(
        route='sitemap.xml',
        view=sitemaps_views.index,
        kwargs={'sitemaps': apps_sitemap},
        name='django.contrib.sitemaps.views.index',
    ),
    path(
        route='sitemap-<section>.xml',
        view=sitemaps_views.sitemap,
        kwargs={'sitemaps': apps_sitemap},
        name='django.contrib.sitemaps.views.sitemap',
    ),
    ## Apps.
    path(route='', view=include('home.urls')),
    path(route='accounts/', view=include('accounts.urls')),
]

## Rosetta.
## http://127.0.0.1:8000/rosetta/
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns.append(path(route='rosetta/', view=include('rosetta.urls')))

if settings.DEBUG:
    ## Static files (dev).
    urlpatterns += static(
        prefix=settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    ## Django debug toolbar.
    if not settings.TESTING:
        import debug_toolbar

        urlpatterns.append(
            path(route='__debug__/', view=include(debug_toolbar.urls)),
        )
