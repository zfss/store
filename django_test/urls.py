# coding=utf-8
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from coltrane.models import Entry

# Uncomment the next two lines to enable the admin:

#这一行不能少，如果少了管理员不能编辑
admin.autodiscover()
entry_info_dict = {
		'queryset': Entry.objects.all(),
		'date_field': 'pub_date',
		}


urlpatterns = patterns('django.views.generic.date_based',
	# url(r'', include('django.contrib.flatpages.urls')),
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
	  #url(r'^weblog/$', 'coltrane.views.entries_index'),	
	  url(r'^weblog/$', 'archive_index',\
		  entry_info_dict),
	  url(r'^weblog/(?P<year>\d{4})/$', 'archive_year',
		  entry_info_dict),
	  url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month',
		  entry_info_dict),
	  url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', 
		  entry_info_dict),
	  url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail',
		  entry_info_dict),
)

urlpatterns += patterns('',
		url(r'^admin/', include(admin.site.urls)),
		url(r'^search/$', 'django_test.search.views.search'),
		url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root':\
			  '/home/administrator/workspace/django_test/tiny_mce/' }),
		url(r'', include('django.contrib.flatpages.urls')),
		)
