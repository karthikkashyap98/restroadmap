from rest_framework import serializers
from .models import Roadmap, Milestone, Action

		
class ActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Action
		fields = ('id','title','body')
		
class MilestoneSerializer(serializers.ModelSerializer):
	actions = ActionSerializer(many=True)
	class Meta:
		model = Milestone
		fields = ('id','title','body','actions')
		depth = 1

class RoadmapSerializer(serializers.ModelSerializer):
	milestones = MilestoneSerializer(many=True)
	class Meta:
		model = Roadmap
		fields = ('id','title','body','milestones')
		depth = 1


class RoadmapCatalogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Roadmap
		fields = ('id','title','body')
