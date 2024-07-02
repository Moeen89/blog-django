from django.urls import path

from . import views
app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("search", views.IndexView.as_view(), name="search"),
    path("post/<int:pk>/",views.DetailsView.as_view(),name="details"),
    path("new_post/",views.NewPostView.as_view(),name="new_post"), 
    path("post/<int:pk>/edit/",views.EditPostView.as_view(),name="edit"),   
    path("post/<int:pk>/delete/",views.DeletePostView.as_view(),name="delete"),   
 
]