from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cvprofile(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    bio = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='cv_picture')
    bio_2 = models.TextField()
    cvfile = models.FileField(upload_to='pdfs/', max_length=100)

    def __str__(self) -> str:
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    download = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='cv_picture')

class Education(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    field_of_study = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)


class Exprience(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=1150)
    company = models.CharField(max_length=50)



class Skills(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="cv_picture")
    description = models.TextField()


class MainPic(models.Model):
    pic = models.ImageField(upload_to='cv_picture')

class Information(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)


class ContactMsg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    msg = models.CharField(max_length=1500)


class Presentation(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    file = models.FileField(upload_to='pdfs/', max_length=100)


    def __str__(self):
        return self.title