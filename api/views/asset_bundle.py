from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, generics, mixins
from rest_framework.response import Response
from api.models import AssetBundle
from api.serializers.asset_bundle import AssetBundleSerializer, AssetBundleDetailSerializer



class AssetBundleList(generics.ListCreateAPIView):
    """
    item create or list view
    """

    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleSerializer

    def list(self, request):
        self.serializer_class = AssetBundleSerializer
        return super(AssetBundleList, self).list(request)


class AssetBundleDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Read Write and Delete Viewe
    """

    queryset = AssetBundle.objects.all()
    serializer_class = AssetBundleDetailSerializer
    
    def retrieve(self, request, pk):
        queryset = self.get_object()
        serializer = AssetBundleDetailSerializer(queryset, many=False)
        return Response(serializer.data)
