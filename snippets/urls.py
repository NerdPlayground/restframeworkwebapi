from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetAPIView,SnippetDetailAPIView

urlpatterns = [
    path('snippets/',SnippetAPIView.as_view()),
    path('snippets/<int:pk>/',SnippetDetailAPIView.as_view())
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