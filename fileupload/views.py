from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from . serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import views
from rest_framework.parsers import FileUploadParser
import xml.dom.minidom
# Create your views here.

class FileUploadView(ListCreateAPIView):
    serializer_class = fileuploadserializer
    queryset = Files.objects.all()
    # renderer_classes = (FileUploadParser, )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GetFileView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = getFileSerializer
    queryset = Files.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        doc = xml.dom.minidom.parse(instance.file)
        expertise = doc.getElementsByTagName("ReportItem")
        dataList = []
        for tags in expertise:
            tagname = tags.getElementsByTagName("plugin_name")
            plugin_name = "".join(t.nodeValue for t in tagname[0].childNodes if t.nodeType == t.TEXT_NODE)
            desc = tags.getElementsByTagName("description")
            description = " ".join(t.nodeValue for t in desc[0].childNodes if t.nodeType == t.TEXT_NODE)
            risk = tags.getElementsByTagName("risk_factor")
            risk_factor = " ".join(t.nodeValue for t in risk[0].childNodes if t.nodeType == t.TEXT_NODE)
            data = plugin_name,description,risk_factor
            dataList.append(data)
        # print(dataList)
        serializer = self.get_serializer(dataList)
        return Response(serializer.data)
