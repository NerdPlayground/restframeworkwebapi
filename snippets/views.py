from django.http import Http404
from rest_framework import status
from snippets.models import Snippet
from rest_framework import renderers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework.response import Response
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import APIView,api_view,action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class SnippetViewSet(ModelViewSet):
    queryset= Snippet.objects.all()
    serializer_class= SnippetSerializer
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    @action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet= self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

'''
# ===> View Classes <====
@api_view(['Get'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format),
    })

class UserAPIView(APIView):

    def get(self,request):
        snippets= User.objects.all()
        serializer_context= { 'request':request }
        serializer= UserSerializer(snippets,many=True,context=serializer_context)
        return Response(serializer.data)
    
    def post(self,request):
        data= request.data
        serializer_context= { 'request':request }
        serializer= UserSerializer(data=data,context=serializer_context)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):

    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        snippet= self.get_object(pk=pk)
        serializer_context= { 'request':request }
        serializer= UserSerializer(snippet,context=serializer_context)
        return Response(serializer.data)

    def put(self,request,pk):
        snippet= self.get_object(pk=pk)
        serializer_context= { 'request':request }
        serializer= UserSerializer(snippet,data=request.data,context=serializer_context)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        snippet= self.get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self,request,format=None):
        snippets= Snippet.objects.all()
        serializer_context= { 'request':request }
        serializer= SnippetSerializer(snippets,many=True,context=serializer_context)
        return Response(serializer.data)

    def post(self,request,format=None):
        data= request.data
        serializer_context= { 'request':request }
        serializer= SnippetSerializer(data=data,context=serializer_context)
        # an alternative
        # serializer.is_valid(raise_exception=True)
        # return Response(serializer.data,status=status.HTTP_200_OK)
        if serializer.is_valid() == True:
            serializer.save(owner=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SnippetDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        snippet= self.get_object(pk=pk)
        serializer_context= { 'request':request }
        serializer= SnippetSerializer(snippet,context=serializer_context)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        snippet= self.get_object(pk)
        serializer_context= { 'request':request }
        serializer= SnippetSerializer(snippet,data=request.data,context=serializer_context)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        snippet= self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetHighlightAPIView(GenericAPIView):
    queryset= Snippet.objects.all()
    renderer_classes= [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet= self.get_object()
        return Response(snippet.highlighted)
'''

'''
# ===> Generic Class Based Views <===
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class SnippetAPIView(ListCreateAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer
'''

'''
# ===> Mixins and Class Based Views <===
from snippets.models import Snippet
from rest_framework.generics import GenericAPIView
from snippets.serializers import SnippetSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class SnippetAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SnippetDetailAPIView(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset= Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
'''

'''
# ===> FUNCTION BASED VIEWS <===
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from snippets.serializers import SnippetSerializer

# clients won't have csrf token
# The server won't check for the token
# The request won't be rejected

@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets= Snippet.objects.all()
        serializer= SnippetSerializer(snippets,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer= SnippetSerializer(data=data)
        if serializer.is_valid() == True:
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet= Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer= SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data= JSONParser().parse(request)
        serializer= SnippetSerializer(snippet,data=data)
        if serializer.is_valid() == True:
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
'''