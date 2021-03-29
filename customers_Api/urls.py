from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.showAll, name='customers'),
    path('customers/<int:id>', views.showOne, name='customers'),

]
