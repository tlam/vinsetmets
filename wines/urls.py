from django.conf.urls import url

from wines import views


app_name = 'wines'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
