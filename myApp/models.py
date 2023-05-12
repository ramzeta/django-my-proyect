from django.db import models


# Create your models here.
class IrisData(models.Model):
    sepal_length = models.DecimalField(max_digits=4, decimal_places=1)
    sepal_width = models.DecimalField(max_digits=4, decimal_places=1)
    petal_length = models.DecimalField(max_digits=4, decimal_places=1)
    petal_width = models.DecimalField(max_digits=4, decimal_places=1)
    species = models.CharField(max_length=50)

    def __str__(self):
        return f"Sepal Length: {self.sepal_length}, Sepal Width: {self.sepal_width}, Petal Length: {self.petal_length}, Petal Width: {self.petal_width}, Species: {self.species}"
