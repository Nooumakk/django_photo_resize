import datetime
import hashlib
from PIL import Image
from pathlib import Path
from django.db import models
from django.utils.safestring import mark_safe


class Photo(models.Model):
    def _load_to(self, filename):
        now = datetime.datetime.now()
        path = datetime.datetime.strftime(now, f"%Y/%m/")
        file, ext = filename.split(".")
        filename = f"{hashlib.md5(file.encode()).hexdigest()}.{ext}"
        return path + filename
    
    photo = models.ImageField(upload_to=_load_to, unique=True)
    width = models.IntegerField()
    height = models.IntegerField()
    slug = models.SlugField(max_length=36, blank=True, unique=True)

    def save(self, *args, **kwargs):
        image = Image.open(self.photo)
        salt = f"{self.width}{self.height}"
        hash_photo = hashlib.md5(image.tobytes() + salt.encode()).hexdigest()
        self.slug = hash_photo
        super(Photo, self).save(*args, **kwargs)
        new_image = image.resize((self.width, self.height))
        new_image.save(self.photo.path)

        
    def blog_img_path(self):
        photo_path = Path(self.photo.url)
        return photo_path

    def blog_img(self):
        return mark_safe('<img class="img-fluid rounded float-left mr-5 mb-4" src="/static{}" alt="post-thumb"/>'.format(self.blog_img_path()))    