from django.contrib import admin
from django.urls import path
from .views import home
from .views import main
from .views import mainlog
from .views import psignup
from .views import docsignup
from .views import plogin
from .views import doclogin
from .views import logout
from .views import dochome
from .views import about
from .views import services
from .views import appointment

urlpatterns = [
    path('', home, name="home"),
    path('main.html', main, name="main"),
    path('mainlog.html', mainlog, name="mainlog"),
    path('psignup.html', psignup, name="psignup"),
    path('docsignup.html', docsignup, name="docsignup"),
    path('plogin.html', plogin, name="plogin"),
    path('doclogin.html', doclogin, name="doclogin"),
    path('logout', logout),
    path('dochome.html', dochome, name="dochome"),
    path('about.html', about),
    path('services.html', services),
    path('appointment.html', appointment, name="appointment"),
]