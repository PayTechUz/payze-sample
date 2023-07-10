from django.urls import path

from apps.payment.views.pay import PayAPIView
from apps.card.views.accept import CardAccceptAPIView
from apps.callback.views import CallBackURLAPIView
from apps.order.views.create import CreateOrderAPIView


urlpatterns = [
    # card
    path('accept/', CardAccceptAPIView.as_view(), name='accept'),

    # callback
    path('success/', CallBackURLAPIView.as_view(), name='success'), 
    
    # order
    path('order/', CreateOrderAPIView.as_view(), name='create'),
    
    # order
    path("pay/", PayAPIView.as_view(), name='pay'), 
]
