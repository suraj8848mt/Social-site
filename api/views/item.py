from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from api.models import Item
from api.serializers import ItemSerializer, ItemDetailSerializers




# @csrf_exempt
# def itemList(request, pk=None):
#     ''' list all items '''

#     if request.method == 'GET':
#         if pk > 0:
#             item = Item.objects.get(pk=pk)
#             serializer = ItemSerializer(item, many=False)
#             return JsonResponse(serializer.data, safe=False)
#         items = Item.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return JsonResponse(serializer.data, safe=False)
        
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ItemSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


class ItemList(generics.ListCreateAPIView):
    """
    item create or list view
    """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        self.serializer_class = ItemSerializer
        return super(ItemList, self).list(request)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Read Write and Delete Viewe
    """

    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializers
    
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = ItemDetailSerializers(queryset, many=False)
        return Response(serializer.data)
