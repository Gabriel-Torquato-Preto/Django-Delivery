import uuid

from django.db import models

# Create your models here.
class User (models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length= 100, default="insert a name", editable=True)
    password = models.TextField(max_length=100, default="insert a password", editable=True)
    phone_number = models.TextField(max_length=100, default="insert a phone number", editable=True)
    email = models.EmailField(default="insert a e-mail")

    def __str__(self) -> models.UUIDField:
        return self.id_user
class Menu(models.Model):
    id_food = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=100, default="insert a name", editable=True)
    description = models.TextField(max_length=1000, default="insert a description", editable=True)
    short_description = models.TextField(max_length=1000, default="insert a description", editable=True)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="assets")

    def __str__(self) -> models.UUIDField:
        return self.id_food


# class FoodRequest(models.Model):
