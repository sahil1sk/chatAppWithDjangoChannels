from django.urls import path, re_path
from .views import index, room

app_name = 'chat'

urlpatterns = [
	path('', index, name='index'),
	#path('<str:room_name>/', room, name='room'),   # so here we make regular expression for getting the room name
	re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]

#re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),