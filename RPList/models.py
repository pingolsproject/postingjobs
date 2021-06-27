from django.db import models



class Company(models.Model):
	Ccompanyname = models.TextField(default='')
	Aaddress = models.TextField(default='')
	class meta:
		db_table = "acompany"


class Companyinfo(models.Model):
	Bbackground = models.TextField(default='')
	Ccapabilities = models.TextField(default='')
	Accreditations= models.TextField(default='')
	Sstakeholder= models.TextField(default='')
	company= models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
	class meta:
	   db_table = "acompanyinfo"


class Jobinformation(models.Model):
	Jjobtitle = models.TextField(default='')
	Jjobvacancy = models.TextField(default='')
	Jjobskillsandqualifications = models.TextField(default='')
	Pposition = models.TextField(default='')
	Jjobresponsibilities = models.TextField(default='')
	Jjobsalary = models.TextField(default='')
	companyinfo= models.ForeignKey(Companyinfo, default=None, on_delete=models.CASCADE)
	class meta:
	   db_table = "aJobinformation"


class Jobrequirements(models.Model):
	Rresume = models.TextField(default='')
	jobinformation = models.ForeignKey(Jobinformation, default=None, on_delete=models.CASCADE)
	class meta:
	   db_table = "aJobrequirements"


class Jobstatus(models.Model):
	Ddate = models.TextField(default='')
	Rremarks = models.TextField(default='')
	jobrequirements = models.ForeignKey(Jobrequirements, default=None, on_delete=models.CASCADE)
	class meta:
	  db_table = "aJobstatus"
	


	










































