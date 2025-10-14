from django.urls import path
from accounts.views.accounts import index, login_view, logout_view, gerencia_view, home_view

urlpatterns = [
    path('', index, name='index'),
    path('home/', home_view, name='home'),
    path('gerencia/', gerencia_view, name='gerencia'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]