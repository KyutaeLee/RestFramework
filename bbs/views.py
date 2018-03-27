from django.shortcuts import render
from .models import Bbs
from .serializers import BbsSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def bbs_list(request, format=None):
    if request.method == 'GET':
        bbs = Bbs.objects.all()
        serializer = BbsSerializers(bbs, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = BbsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST', 'DELETE'])
def bbs_detail(request, pk, format=None):
    try:
        bbs = Bbs.objects.get(pk=pk)
    except Bbs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BbsSerializers(Bbs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BbsSerializers(bbs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bbs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


