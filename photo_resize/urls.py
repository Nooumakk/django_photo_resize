from django.urls import path
from .views import PhotoApiCreateViev, PhotoVievs



urlpatterns = [
    path("api/v1/photoresize", PhotoApiCreateViev.as_view(), name = "photo"),
    path("<slug:slug>/", PhotoVievs.as_view(), name="single_photo")
]
