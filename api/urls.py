from django.urls import path 
from . import views



urlpatterns = [
    
    # USER PATTERNS
    
    path('', views.getData),
    path('login', views.login),
    path('register', views.register),
    path('user_data', views.user_data),
    
    
    # TICKET PATTERNS
    path('create', views.createTicket),
    path('blog/<int:id>', views.blogDetail)
    

]

