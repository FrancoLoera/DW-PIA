from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_personalizado, name='login'),
    path(
    'logout/',
    auth_views.LogoutView.as_view(
        next_page='index',
        http_method_names=['get', 'post']
    ),
    name='logout'
),

]


