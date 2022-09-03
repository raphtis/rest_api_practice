from django.urls import path 
from . import views


urlpatterns = [
    path('', views.getData),
    path('create', views.createTicket),
    path('item/<int:id>', views.itemDetail)
]

