from django.urls import path 
from . import views


urlpatterns = [
    
    # USER PATTERNS
    
    path('', views.getData),
    
    
    # TICKET PATTERNS
    path('create', views.createTicket),
    path('item/<int:id>', views.itemDetail)
    

]

