from django.urls import URLPattern, path
from  . import views

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    
] 