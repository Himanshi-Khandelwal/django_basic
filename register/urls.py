from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import (
	base,
	signup,
	logout_view,
	detail,
	post_create,
	show_list
	)

urlpatterns = [
	url(r'^$', base , name='base'),
	url(r'^create/$', post_create, name='create'),
	url(r'^show_list/$', show_list , name='show_list'),
	#url(r'^create/detail/$', detail, name='detail'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', logout_view,  name='logout'),
	url(r'^signup/$', signup, name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
