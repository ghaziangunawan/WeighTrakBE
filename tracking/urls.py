from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tracking.views import *

urlpatterns = [
    path('session/', SessionViews.as_view()),
    path('me/', MeViews.as_view()),
    path('me/<int:pk>/', MeUpdateView.as_view()), 
]


urlpatterns = format_suffix_patterns(urlpatterns)