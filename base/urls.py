from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('details/<int:pk>/',views.details,name='details'),
    path('addtocart/<int:pk>/',views.addtocart,name='addtocart'),
    path('remove/<int:pk>/',views.remove,name='remove'),
    path('support',views.support,name='support')
]
