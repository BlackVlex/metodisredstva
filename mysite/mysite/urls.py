from django.contrib import admin
from django.urls import path
from blog.views import home, post_list, about, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', post_list, name='post_list'),
    path('about/', about, name='about'),
    path('blog/create/', post_create, name='post_create'),
    path('blog/<int:pk>/', post_detail, name='post_detail'),
    path('blog/<int:pk>/edit/', post_edit, name='post_edit'), 
     path('blog/<int:pk>/delete/', post_delete, name='post_delete'),
]