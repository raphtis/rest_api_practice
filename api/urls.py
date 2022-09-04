from django.urls import path 
from . import views



urlpatterns = [
    
    # USER PATTERNS
    
    path('', views.getData),
    path('users', views.getUsers),

    
    
    # TICKET PATTERNS
    path('create', views.createTicket),
    path('blog/<int:id>', views.blogDetail)
    

]

