from django.db import models

from django.contrib.auth.models import User,AbstractUser


# Create your models here.


class MyUser(AbstractUser):
    phone=models.CharField(max_length=12)
    profile_pic=models.ImageField(null=True,upload_to="profilepics")    

class Postuploads(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")
    caption=models.CharField(max_length=500)
    post_like=models.ManyToManyField(MyUser,related_name="postlike")
    posted_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.caption

class Comments(models.Model):
    post=models.ForeignKey(Postuploads,on_delete=models.CASCADE)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)



    

    