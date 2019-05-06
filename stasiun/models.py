from django.db import models

# Create your models here.
class Stasiun_models(models.Model):
	nama = models.CharField(primary_key=True, max_length=10)
	alamat = models.CharField(max_length=50)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	class Meta:
		db_table = 'STASIUN'