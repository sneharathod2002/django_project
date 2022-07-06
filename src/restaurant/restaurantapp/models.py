from django.db import models

# Create your models here.
class restaurants_list(models.Model):
    Reataurant_name = models.CharField(max_length = 100)
    Description = models.TextField(blank=True, null=True)
    Location = models.TextField(blank=False, null=False)
    Cuisines = models.ManyToManyField("Cuisines")
    veg = models.BooleanField()
    Rating = models.FloatField()
    Contect_no = models.CharField(max_length=10)
    Email = models.EmailField()

    def __str__(self) -> str:
        return self.Reataurant_name

class Cuisines(models.Model):
    Cuisions_type = models.CharField(max_length= 120)

    def __str__(self) -> str:
        return self.Cuisions_type

class Menu (models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField(blank = False, null= False)
    Cuision_type = models.ForeignKey("Cuisines", on_delete=models.CASCADE)
    Price = models.IntegerField()
    veg = models.BooleanField()

    def __str__(self) -> str:
        return self.Name

