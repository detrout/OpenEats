from __future__ import absolute_import

from django.contrib.auth.views import login
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView
from accounts.forms import ProfileForm
from accounts.views import logout_page, signIn_page
from recipe.views import index
from profiles.views import edit_profile

import helpers.signals  #needed to import the signal for when a user is saved their profile is created
from registration.views import RegistrationView
from relationships.listeners import attach_relationship_listener
attach_relationship_listener()
register = RegistrationView.as_view()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^accounts/logout/$', logout_page, name='logout_page'),
    url(r'^accounts/signIn/$', signIn_page),
    url(r'^accounts/ajax-signIn/$', login, {'template_name': 'accounts/ajax_signIn.html',}),
    url(r'^accounts/ajax-create/$', register, {'backend': 'registration.backends.default.DefaultBackend','template_name': 'accounts/ajax_create.html',}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/edit', edit_profile, {'form_class': ProfileForm,}),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^follow/', include('relationships.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^feed/', include('feed.urls')),
    url(r'^groups/', include('recipe_groups.urls')),
    url(r'^recipe/', include('recipe.urls')),
    url(r'^ingredient/', include('ingredient.urls')),
    url(r'^list/', include('list.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^$', index),
]



if settings.SERVE_MEDIA:
    urlpatterns += [
        url(r'^site-media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
        ]
#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += [
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    ]
