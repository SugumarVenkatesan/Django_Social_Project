from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings  # New Import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_social_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url('', include(
                           'social.apps.django_app.urls', namespace='social')),
                       url(r'^$', 'django_social_app.views.login'),
                       url(r'^home/$', 'django_social_app.views.home'),
                       url(r'^update_status/$',
                           'django_social_app.views.post_tweet'),
                       url(r'^delete/$', 'django_social_app.views.delete'),
                       url(r'^logout/$', 'django_social_app.views.logout'),
                       )


# urlpatterns += static(settings.STATIC_URL,
# document_root=settings.STATIC_ROOT)# New Import
