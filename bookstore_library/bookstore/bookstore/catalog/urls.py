from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',views.catalog, name='index'),
    url(r'^book/(?P<pk>\d+)$', views.book_detail_view, name='book-detail'),
]
