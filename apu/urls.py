from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('roadmap', views.RoadmapView)


urlpatterns = [
 	
 	path('', include(router.urls))
 	# path('action/done/<int:id>/', views.progress)
	# path('roadmap/', views.RoadmapView.as_views())
 ]
