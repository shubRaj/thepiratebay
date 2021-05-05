from django.urls import path,re_path
from . import views
app_name = "app_pirate"
urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    re_path(r"^search/?(?P<query>[\w \(\)-\.:\[\]]*)?/$",views.Search.as_view(),name="search"),
]