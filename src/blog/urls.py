from django.conf.urls import url
from .views import post, archives, PostCreate

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^archives/$', archives, name='archives'),
    # url(r'^post/$', post_page_view, name='detail'),
    url(r'^post/(?P<pk>\d+)/$', post, name='post'),
    url(r'^create/$',PostCreate.as_view(), name='create'),
]
