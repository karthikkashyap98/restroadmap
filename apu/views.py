from django.shortcuts import render, HttpResponse
from . models import Roadmap, Milestone
from . serializers import RoadmapSerializer, MilestoneSerializer
from rest_framework import viewsets


def home(request):

	return HttpResponse('HOMEBITCH')


class RoadmapView(viewsets.ModelViewSet):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer

    @action(detail=False, methods=['GET'])
    def filter_milestone(self, pk):
    	road = Roadmap.objects.get(pk=id)
    	milestones = Milestone.objects.filter(roadmaplink=road)
    	queryset = milestones
    	serializer_class = MilestoneSerializer
		

# @action(detail=False, methods=['GET'])
# def filter_shippings(self, request, **kwargs):
#     queryset = self.get_queryset().filter(status=2, orderStatus=0)
#     serializer = SearchShippingSerializer(queryset, many=True) #Yes, I am using another serializer, but it is solved,I use diferent if it is necesary
#     return Response(serializer.data)