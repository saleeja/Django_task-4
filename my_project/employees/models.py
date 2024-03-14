from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

