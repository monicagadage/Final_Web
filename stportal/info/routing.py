from django.urls import path

from . import consumers

websocket_urlpatterns = [
      
      path('ws/info/room/<str:room_name>/<str:username>/', consumers.ChatConsumer.as_asgi()),
      # path('ws//', consumers.ChatConsumer.as_asgi()), # Using asgi

    # re_path(r'ws/info/room/(<str:room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]