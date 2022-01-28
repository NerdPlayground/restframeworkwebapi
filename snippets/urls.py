from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetAPIView,SnippetDetailAPIView,UserAPIView,UserDetailAPIView,SnippetHighlightAPIView

urlpatterns = [
    path('users/',UserAPIView.as_view()),
    path('users/<int:pk>/',UserDetailAPIView.as_view()),
    path('snippets/',SnippetAPIView.as_view()),
    path('snippets/<int:pk>/',SnippetDetailAPIView.as_view()),
    path('snippets/<int:pk>/highlight/',SnippetHighlightAPIView.as_view())
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