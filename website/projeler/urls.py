from django.urls import path
from . import views 

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/projelerim
# http://127.0.0.1:8000/projelerim/1

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home_redirect"),
    path("projeler/<int:id>", views.projedetay, name="detaylar"),
]