from django.conf.urls import url

from cuisines import views


app_name = 'cuisines'
urlpatterns = [
    url(r'^data.json$', views.json_data, name='index')
]
