from django.contrib import admin
from django.conf.urls import url

from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

from maps.views import MapReleaseView, MapFixView


class DDNetAdmin(admin.AdminSite):
    site_header = 'DDNet Administration'

    def get_urls(self):
        urls = super().get_urls()

        extra_urls = [
            url(r'^maps/maprelease/(?P<pk>[0-9]+)/release', MapReleaseView.as_view()),
            url(r'^maps/mapfix/(?P<pk>[0-9]+)/fix', MapFixView.as_view())
        ]

        return urls + extra_urls


site = DDNetAdmin()
MapReleaseView.admin = site
MapFixView.admin = site

site.register(Group, GroupAdmin)
site.register(User, UserAdmin)
