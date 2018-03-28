from .models import Bbs
from .serializers import BbsSerializers
from rest_framework import generics

class BbsList(generics.ListCreateAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializers

class BbsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bbs.objects.all()
    serializer_class = BbsSerializers
