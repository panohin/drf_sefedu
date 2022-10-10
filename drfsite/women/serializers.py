import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from . import models


class WomenSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Women
		fields = ('id','title', 'content', 'category')
		# fields = ('__all__')

# class WomenModel:
# 	'''
# 	Имитация модели Django
# 	'''
# 	def __init__(self, title, content):
# 		self.title = title
# 		self.content = content

# class WomenSerializer(serializers.Serializer):
# 	title = serializers.CharField(max_length=50)
# 	content = serializers.CharField()
# 	time_create = serializers.DateTimeField(read_only=True)
# 	time_update = serializers.DateTimeField(read_only=True)
# 	is_published = serializers.BooleanField(default=True)
# 	category_id = serializers.IntegerField()

# 	def create(self, validated_data):
# 		return models.Women.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title = validated_data.get('title', instance.title)
# 		instance.content = validated_data.get('content', instance.content)
# 		instance.time_update = validated_data.get('time_update', instance.time_update)
# 		instance.is_published = validated_data.get('is_published', instance.is_published)
# 		instance.category_id = validated_data.get('category_id', instance.category_id)
# 		instance.save()
# 		return instance

# def encode():
# 	'''
# 	Из модели в JSON
# 	'''
# 	model = WomenModel('Pavel', 'Anohin')
# 	model_sr = WomenSerializer(model)
# 	print(model_sr, type(model_sr.data), sep='\n')
# 	json = JSONRenderer().render(model_sr.data)
# 	print(json)

# def decode():
# 	'''
# 	Из строки в словарь
# 	'''
# 	stream = io.BytesIO(b'{"title":"Pavel","content":"Anohin"}')
# 	data = JSONParser().parse(stream)
# 	serializer = WomenSerializer(data=data)
# 	serializer.is_valid()
# 	print(serializer.validated_data)