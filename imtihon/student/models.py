from django.db import models

# Create your models here.
class Cities(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)
    about=models.TextField(null=True, blank=True)
    price=models.IntegerField()
    Image=models.ImageField(null=True, blank=True, verbose_name='image', upload_to='city/')
    cat=models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, )
    air=models.ManyToManyField('AirWays',null=True, blank=True, related_name='city')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Shahar'
        verbose_name_plural='Shaharlar'

class Category(models.Model):
    name=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class AirWays(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
 
    class Meta:
        verbose_name="Air company"
        verbose_name_plural="Air companys"
    