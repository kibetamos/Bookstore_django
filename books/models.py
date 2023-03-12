from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  
  
  def __str__ (self):
    return self.title
  
#   Below we’ve specified a __str__ method to control how the object is outputted in the Admin and
# Django shell.