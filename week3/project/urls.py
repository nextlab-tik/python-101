from django.conf.urls import url, include  # add include
from django.contrib import admin
# import app.urls  # importer les urls de l'application

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('app.urls')),  # ajouter les urls de l'app
]
