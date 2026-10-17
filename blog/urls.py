from django.urls import path
from blog.views import home, about, post_details

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("post/<int:pk>/", post_details, name="post_detial"),

]