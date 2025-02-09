from tracking.models import *
from tracking.serializers import *
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
class SessionViews(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class MeViews(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Me.objects.all()
    serializer_class = MeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class MeUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Me.objects.all()
    serializer_class = MeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)