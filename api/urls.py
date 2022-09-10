from django.urls import path 
from knox import views as knox_views
from . import views



urlpatterns = [
    
    # USER PATTERNS
    
    path('', views.getData),
    path('login', views.login),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('register', views.register),
    path('user_data', views.user_info),
    
    
    # TICKET PATTERNS
    path('create', views.createTicket),
    path('blog/<int:id>', views.blogDetail)
    

]

