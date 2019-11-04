from django.urls import path,include
from django.conf.urls import include, url   
from .import views

urlpatterns = [
    path("h", views.blog_index, name="b_index"),
    path("<int:pk>/", views.blog_detail, name="b_detail"),
    path("Ask/",views.Ask_Form,name="ask"),
    path("<int:pk>/edit", views.post_update.as_view(), name="edit"),
    path("<int:pk>/delete", views.post_delete.as_view(), name="delete"),
    
]