from django.db import models

class Sepeda_models(models.Model):
	merk = models.CharField(primary_key=True, max_length=10)
	jenis = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	stasiun = models.CharField(max_length=10)
	penyumbang = models.CharField(max_length=20)
	class Meta:
		db_table = 'SEPEDA'