from django.db import models


class DjangoClasses(models.Model):
    Tittle = models.CharField(max_length=60)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
