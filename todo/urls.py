from django.conf.urls import url

from todo import views

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_todo/', views.add_todo, name='add_todo'),
    url(r'^delete_todo/(?P<id>\d+)$', views.delete_todo, name='delete_todo'),
]
