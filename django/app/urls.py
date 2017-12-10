from django.conf.urls import url
from .views import index, contact, PostList, PostDetail

urlpatterns = [
    url('^$', PostList.as_view()),
    url('^contact/?$', contact),
    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view(), name="post_detail"),
]
