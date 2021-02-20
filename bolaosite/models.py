from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Jogo(models.Model):
	
	id = models.AutoField(primary_key=True, unique=True)
	rodada = models.CharField(max_length=200)
	time1 = models.CharField(max_length=200)
	time2 = models.CharField(max_length=200)
	data_hora = models.CharField(max_length=200)
	gols_time1 = models.CharField(max_length=200)
	gols_time2 = models.CharField(max_length=200)


class Aposta(models.Model):
	
	#caixa de seleção, ver depois
	user = models.CharField(max_length=200)

	def saveTxt(self):
		pass