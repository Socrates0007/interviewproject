from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from .models import Template
from .serializers import TemplateModelSerializer


from .models import Template

# Create your views here. good

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def template_list_view(request):
    templates=Template.objects.all()
    if request.method=="GET":
        serializer_class=TemplateModelSerializer(templates, many=True)
        return Response(serializer_class.data)
    elif request.method=='POST':
        serializer_class=TemplateModelSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
 
@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def template_detail_view( request, pk):
    template= get_object_or_404(Template, pk=pk)
    if request.method=="GET":
        serializer_class=TemplateModelSerializer(template)
        return Response(serializer_class.data)
    elif request.method=="PUT":
        serializer_class=TemplateModelSerializer(template, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
    elif request.method=="DELETE":
        template.delete()
        return Response({})
 