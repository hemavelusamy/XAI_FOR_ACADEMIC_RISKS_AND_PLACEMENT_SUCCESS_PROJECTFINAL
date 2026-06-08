from django.db import models

class Students(models.Model):
    register_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    cgpa = models.FloatField()
    attendance = models.FloatField()
    
    def __str__(self):
        return self.name