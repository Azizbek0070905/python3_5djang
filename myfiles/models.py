from django.db import models


# Create your models here.

class Services(models.Model):
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=20)
    malumot = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Type(models.Model):
    turi = models.CharField(max_length=30)

    def __str__(self):
        return self.turi


class Portfolio(models.Model):
    img = models.ImageField(upload_to='media')
    # image = models.ImageField(upload_to='media')
    # rasm = models.ImageField(upload_to='media')
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    date = models.DateField()
    link = models.CharField(max_length=40)
    matn = models.TextField()


class Kasbi(models.Model):
    hodim = models.CharField(max_length=50)

    def __str__(self):
        return self.hodim


class Team(models.Model):
    name = models.CharField(max_length=30)
    kasbi = models.ForeignKey(Kasbi, on_delete=models.CASCADE)
    malumot = models.TextField()
    img = models.ImageField(upload_to="media")
    twit = models.CharField(max_length=40)
    face = models.CharField(max_length=40)
    inst = models.CharField(max_length=40)
    tele = models.CharField(max_length=40)
    date = models.DateTimeField()


class Contact(models.Model):
    nomi = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mavzu = models.CharField(max_length=50)
    matn = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Subcribe(models.Model):
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now=True)


class Subcribe1(models.Model):
    gmail = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now=True)
