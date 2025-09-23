from django.urls import path
from .views import login_view, index, logout_view, home_view, gerencia_view

urlpatterns = [
    path('', index, name='index'),
    path('home/', home_view, name='home'),
    path('gerencia/', gerencia_view, name='gerencia'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]