from django.db import models


class Roadmap(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	
	def __str__(self):
		return f"{self.title}"


class Milestone(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	roadmaplink = models.ForeignKey(Roadmap, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title}"

	@property
	def actions(self):
		actions = Action.objects.filter(milestonelink=self).values('id', 'title', 'body')
		return list(actions)

class Action(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	milestonelink = models.ForeignKey(Milestone, on_delete=models.CASCADE)


	def __str__(self):
		return f"{self.title}"
