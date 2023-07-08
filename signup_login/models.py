from django.db import models
from django.contrib.auth.models import User
class Signup(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.username)
class house(models.Model):
    address=models.CharField(max_length=264)
    apartment=models.CharField(max_length=264)
    type=models.CharField(max_length=264)
    price=models.IntegerField(null=True)
    owner=models.CharField(max_length=264)
    contact=models.PositiveBigIntegerField()
    img1=models.ImageField(null=True,upload_to='house_pics')
    def __str__(self):
        return str(self.owner)

