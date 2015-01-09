# Copyright (C) 2010-2014 GRNET S.A.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, include, url
from django.contrib import admin

from index import urls as index_urls
from index import tags_urls
from notes import urls as notes_urls
from meetings import urls as meetings_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include(index_urls)),
    url(r'^tags/', include(tags_urls, namespace='tags')),
    url(r'^meetings/', include(meetings_urls, namespace='meetings')),
    url(r'^notes/', include(notes_urls, namespace='notes')),
    url(r'^admin/', include(admin.site.urls)),
)
