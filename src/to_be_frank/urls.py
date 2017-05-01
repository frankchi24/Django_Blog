"""to_be_frank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home,contact,about,post,UserRegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', UserRegisterView.as_view(), name='signup'),
    url(r'^$',home, name='home'),
    url(r'^contact/$',contact, name='contact'),
    url(r'^about/$',about, name='about'),
    url(r'^post/$',post, name='post'),
    url(r'^blog/',include('blog.urls',namespace='blog')),
]


if settings.DEBUG:
	urlpatterns+=(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
