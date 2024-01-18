"""
the provider url patterns.
"""
from django.urls import path

from apps.payment.providers.payze import views


urlpatterns = [
    path('payment/payze/token', views.TokenAPIView.as_view()),
    path('payment/payze/webhook/cards', views.CardsWebHooksAPIView.as_view())
]
