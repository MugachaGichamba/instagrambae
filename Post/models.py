from django.db import models
from django.utils import timezone

# Create your models here.
from users.models import Profile
from django.contrib.auth.models import User
from  PIL import Image
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField(blank=False, upload_to='home_pics')
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def get_absolute_url(self):
        return reverse('insta_home')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.image_name, str(self.user.username))