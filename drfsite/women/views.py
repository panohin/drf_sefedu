from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from .serializers import WomenSerializer


class WomenAPIView(APIView):
	def get(self, request):
		content = models.Women.objects.all()
		return Response({'data': WomenSerializer(content, many=True).data})

	def post(self, request):
		serializer = WomenSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		# post_new = models.Women.objects.create(
		# 	title = request.data['title'],
		# 	content = request.data['content'],
		# 	category_id = request.data['category_id']
		# 	)
		
		return Response({'post': serializer.data})

	def put(self, request, *args, **kwargs):
		pk = kwargs.get('pk', None)
		if not pk:
			return Response({'error':'Method PUT not allowed'})
		try:
			instance = models.Women.objects.get(pk=pk)
		except:
			return Response({'error':'Object does not exist'})
		serializer = WomenSerializer(request.data, instatce=instance)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({'post': serializer.data})

	def delete(self, request, *args, **kwargs):
		pk = kwargs.get('pk', None)
		if not pk:
			return Response({'error':'Method DELETE not allowed'})
		try:
			instance = models.Women.objects.get(pk=pk)
		except:
			return Response({'error':'Object does not exist'})
		instance.delete()
		return Response({'post': f'Object {instance.title} delete'})


# class WomenAPIView(generics.ListAPIView):
# 	queryset = models.Women.objects.all()
# 	serializer_class = WomenSerializer