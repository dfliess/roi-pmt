from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.db.models.functions import Lower

from .serializers import TweetSerializer
from .models import Tweet

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    #must override as we can't use django-filter
    def get_queryset(self):
        ordering = self.request.query_params.get('ordering')
        queryset = Tweet.objects.all().order_by(Lower(ordering))
        return queryset