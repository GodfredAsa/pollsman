from django.urls import path
from . import views
app_name = 'registration'

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('signin/', views.sign_in, name = 'sign_in'),
]