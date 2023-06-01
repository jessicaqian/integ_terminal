from django.urls import path
from . import views

app_name ='system'

urlpatterns = [
    path('main.html', views.main),
    path('audioconfig.html', views.audioConfig),
    path('videoconfig.html', views.videoConfig),
    path('meetcontrol.html', views.meetControl),
    path('netconfig.html', views.netconfig),
    path('UIdisplay.html', views.uiDisplay),
]