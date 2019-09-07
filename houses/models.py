from django.db import models


# Create your models here.

class House(models.Model):
	bariwalar_nam = models.CharField(max_length=100)
	bariwalar_reg_id = models.IntegerField(null=True)
	zilla = models.CharField(max_length=25)
	upazilla = models.CharField(max_length=25)
	elaka = models.CharField(max_length=25)
	family_basha = models.BooleanField(null=True)  # True means family basha, False means mess.
	shobar_ghorer_shongkhya = models.IntegerField(null=True)
	bathroomer_shongkhya = models.IntegerField(null=True)
	khabar_ghor = models.BooleanField(null=True)
	rannaghor = models.BooleanField(null=True)
	barivara = models.IntegerField(null=True)

	# class Meta:
	# 	db_table = 'House'

	def __str__(self):  # Should it be __unicode__(self)?
		return str(self.zilla)
