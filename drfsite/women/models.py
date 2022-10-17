from django.db import models
from django.contrib.auth.models import User

class Women(models.Model):
	title = models.CharField('Загловок', max_length=50)
	content = models.TextField('Контент', blank=True, null=True)
	# photo = models.ImageField('Фотография', blank=True, null=True)
	time_create = models.DateTimeField('Создан', auto_now_add=True)
	time_update = models.DateTimeField('Изменен', auto_now=True)
	is_published = models.BooleanField('Опубликовано', default=True)
	category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['time_create']
		verbose_name = 'Известная женщина'
		verbose_name_plural = 'Известные женщины'

class Category(models.Model):
	name = models.CharField('Название категории', max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'