from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    service = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name