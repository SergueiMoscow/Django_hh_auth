from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('secret/', views.secret_page, name='home'),
    path('registration/', views.signup, name='registration'),
    path('logout/', views.login_view, name='logout')

]