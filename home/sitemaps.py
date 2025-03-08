from django.contrib import sitemaps
from django.urls import reverse


class HomeSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ('home',)

    def location(self, item):
        return reverse(f'home:{item}')
