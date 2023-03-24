import hashlib
import copy
from PIL import Image
from rest_framework import views
from .serializer import PhotoSerializer
from .models import Photo
from django.views import generic
from rest_framework.response import Response


class PhotoVievs(generic.DetailView):
    model = Photo
    template_name = "single_photo.html"


class PhotoApiCreateViev(views.APIView):
    def post(self, request):
        serializer = PhotoSerializer(data=copy.deepcopy(request.data))
        serializer.is_valid(raise_exception=True)
        img = Image.open(request.data["photo"])
        salt = f"{request.data['width']}{request.data['height']}"
        hash_img = f"{hashlib.md5(img.tobytes() + salt.encode()).hexdigest()}"
        try:
            photo = Photo.objects.get(slug=hash_img)
        except Photo.DoesNotExist:
            serializer.save()
            photo = Photo.objects.get(slug=hash_img)
        return Response({"url": f"http://127.0.0.1:8000/{photo.slug}"})
        