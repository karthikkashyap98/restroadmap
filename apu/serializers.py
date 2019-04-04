from rest_framework import serializers
from .models import Roadmap, Milestone, Action


class RoadmapSerializer(serializers.ModelSerializer):
	class Meta:
		model = Roadmap
		fields = ('id','title','body')
		
class MilestoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Milestone
		fields = ('id','title','body')


