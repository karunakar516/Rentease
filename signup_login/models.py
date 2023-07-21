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
    userid=models.CharField(max_length=264)
    houseid=models.IntegerField()
    contact=models.PositiveBigIntegerField()
    img1=models.ImageField(upload_to='house_pics',null=True)
    img2=models.ImageField(upload_to='house_pics',null=True)
    img3=models.ImageField(upload_to='house_pics',null=True)
    def __str__(self):
        return str(self.owner)

class current_signup(models.Model):
    username=models.CharField(max_length=264)
    password=models.CharField(max_length=264)
    reppass=models.CharField(max_length=264)
    email=models.EmailField(max_length=264)
    x=models.IntegerField()