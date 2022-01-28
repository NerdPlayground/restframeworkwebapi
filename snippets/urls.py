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