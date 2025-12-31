from django.urls import path
from .views import register_page,logout_view

app_name = 'user'

urlpatterns = [
    path('register/',register_page,name='register_page'),
    path('logout/', logout_view, name='logout'),
]