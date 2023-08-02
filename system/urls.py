from django.urls import path
from . import views

app_name ='system'

urlpatterns = [
    path('main.html', views.main),
    path('meet.html', views.meet),
    path('meetcontrol.html', views.meetControl),
    path('netconfig.html', views.netconfig),
    path('UIdisplay.html', views.uiDisplay),
    path('time.html', views.time),
    path('secure.html', views.secure),
    path('version.html', views.version),
    path('log.html', views.log),
    path('interfaceControl.html', views.interfaceControl),
    path('sysupdate.html', views.sysUpdate),
    path('sysdiagnosis.html',views.sysdiagnosis),
    path('notify', views.notify),
    path('checkstatus', views.checkStatus),
]