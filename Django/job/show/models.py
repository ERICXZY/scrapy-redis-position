from django.db import models

# Create your models here.
class job(models.Model):
	job_id=models.IntegerField(primary_key=True)
	spider=models.CharField(max_length=128)
	detail_url=models.CharField(max_length=128)
	pos_name=models.CharField(max_length=128)
	salary=models.CharField(max_length=128)
	pub_date=models.CharField(max_length=128)
	edu_bg=models.CharField(max_length=128)
	experience=models.CharField(max_length=128)
	location=models.CharField(max_length=128)
	company=models.CharField(max_length=128)
	pos_desc=models.CharField(max_length=128)
	crawled=models.CharField(max_length=128)
	class Meta:
		db_table='Job'

class Condition(models.Model):
	con_id=models.IntegerField(primary_key=True)
	type_id=models.IntegerField()
	con_str=models.CharField(max_length=128)
	class Meta:
		db_table='Condition'