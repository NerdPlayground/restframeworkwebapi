from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet,UserViewSet

router= DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'snippets',SnippetViewSet)

urlpatterns=[
    path('',include(router.urls))
]

'''
# ===> Explicit URL to View Binding <===
from django.urls import path
from rest_framework import renderers
from snippets.views import api_root,UserViewSet,SnippetViewSet

snippet_list= SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail= SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight= SnippetViewSet.as_view({
    'get': 'highlight'
},renderer_classes= [renderers.StaticHTMLRenderer])

user_list= UserViewSet.as_view({
    'get': 'list'
})

user_detail= UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('',api_root),
    path('users/',user_list,name='user-list'),
    path('users/<int:pk>/',user_detail,name='user-detail'),
    path('snippets/',snippet_list,name='snippet-list'),
    path('snippets/<int:pk>/',snippet_detail,name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',snippet_highlight,name='snippet-highlight'),
]
'''

'''
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import api_root,SnippetAPIView,SnippetDetailAPIView,UserAPIView,UserDetailAPIView,SnippetHighlightAPIView

urlpatterns = [
    path('',api_root),
    path('users/',UserAPIView.as_view(),name='user-list'),
    path('users/<int:pk>/',UserDetailAPIView.as_view(),name='user-detail'),
    path('snippets/',SnippetAPIView.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/',SnippetDetailAPIView.as_view(),name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',SnippetHighlightAPIView.as_view(),name='snippet-highlight'),
]

urlpatterns= format_suffix_patterns(urlpatterns)
'''

'''
# ===> FUNCTION BASED VIEWS <===
from snippets import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('snippets/',views.snippet_list),
    path('snippets/<int:pk>/',views.snippet_detail)
]

urlpatterns= format_suffix_patterns(urlpatterns)
'''