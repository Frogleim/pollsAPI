from django.urls import path

from .views import QuestionViewSet,ChoiceViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',ChoiceViewSet,basename='choices')
router.register('user',UserViewSet, basename='user')

urlpatterns = router.urls
