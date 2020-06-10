from django.db import models



# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=40, default=None, db_index=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    system = models.CharField(max_length=20)
    ram = models.IntegerField()
    pixel = models.IntegerField()
    double_camera = models.BooleanField(default=False)
    cpu = models.CharField(max_length=50)
    screen = models.CharField(max_length=12)
    fm = models.BooleanField(default=False)
    additionally = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name
