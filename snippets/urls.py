from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     path('list', views.SnippetList.as_view(), name='snippet-list'),
#     path('<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
#     path('', views.api_root),
#     path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),

# ]
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
router = DefaultRouter()
router.register(r'', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [path('api-auth/', include('rest_framework.urls'))]

