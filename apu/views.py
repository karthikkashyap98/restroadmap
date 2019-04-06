from django.shortcuts import render, HttpResponse
from . models import Roadmap, Milestone
from . serializers import RoadmapSerializer, MilestoneSerializer, RoadmapCatalogSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


def home(request):

	return HttpResponse('HOMEBITCH')


class RoadmapView(viewsets.ModelViewSet):
	queryset = Roadmap.objects.all()
	serializer_class = RoadmapSerializer
		
	def list(self, request):
		queryset = Roadmap.objects.all()
		serializer = RoadmapCatalogSerializer(queryset, many=True)
		return Response(serializer.data)



			