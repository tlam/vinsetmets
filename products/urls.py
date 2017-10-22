from django.conf.urls import url

from products import views


app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<product_id>\d+)/$', views.show, name='show'),
    url(r'^(?P<product_id>\d+).json$', views.stats, name='stats'),
]
