from django.urls import path
from . import views

urlpatterns = [
    #path('if someone goes here', 'redirect here', 'name of view')
    path('', views.home, name='home'),
    path('new_seacrh', views.new_search, name='new_search'),
]