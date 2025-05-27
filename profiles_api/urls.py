from django.urls import path , include
from profiles_api import views
from rest_framework.routers import DefaultRouter
from .views import HelloViewSet, HelloApiView

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset') # Base name só é usado quando a viewset não possui queryset
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
  path('hello-apiview/', views.HelloApiView.as_view()),
  path('',include(router.urls)) # Aqui ele vai pegar as urls do router
] 