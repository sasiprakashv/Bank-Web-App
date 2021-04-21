from django.db import models

class Bio(models.Model):
   customer_no=models.IntegerField()
   Name=models.CharField(max_length=30)
   Email=models.EmailField()
   Amount=models.IntegerField()

   def __str__(self):
      return f"{self.pk}"
   