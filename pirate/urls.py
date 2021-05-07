from django.urls import path,re_path
from . import views
app_name = "app_pirate"
urlpatterns = [
    re_path(r"^description/(?P<id>\d{7,8})/$",views.Description.as_view(),name="description"),
    re_path(r"^search/(?P<query>[\w \(\)-\.:\[\]]*)?/?$",views.Search.as_view(),name="search"),
    path("",views.Home.as_view(),name="home"),
]