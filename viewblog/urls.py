from django.contrib.auth import views as auth_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_view.LoginView.as_view(template_name = 'logout.html'), name='logout'),
]
