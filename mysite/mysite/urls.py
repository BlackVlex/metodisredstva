from django.contrib import admin
from django.urls import path
from blog.views import home, post_list, about, post_detail  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', post_list, name='post_list'),
    path('about/', about, name='about'),
    path('blog/<int:pk>/', post_detail, name='post_detail'), 
]