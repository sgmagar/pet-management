from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now_add=False)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Name: {}, Birthday: {}'.format(self.name, self.birthday)


class Dog(Pet):
    owner = models.ForeignKey(
        User, related_name='dogs', on_delete=models.CASCADE)


class Cat(Pet):
    owner = models.ForeignKey(
        User, related_name='cats', on_delete=models.CASCADE)
