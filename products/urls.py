from django.conf.urls import url

from products import views


app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
