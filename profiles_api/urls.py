from django.urls import URLPattern, path,include
from  . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profiles',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
    
] 