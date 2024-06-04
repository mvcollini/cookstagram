from django.urls import path
from .views import homepage, home, mylogin, signin, registra, esci, login_view,profilo
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", homepage, name="homepage"),
    path("mylogin/", mylogin, name="mylogin"),
    path("signin/", signin, name="signin"),
    path("home/", home, name="home"),
    path("registra/", registra, name="registra"),
    path("esci/", esci, name="esci"),
    path("login_view/", login_view, name="login_view"),
    path("profilo/", profilo, name='profilo')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
