"""
the provider url patterns.
"""
from django.urls import path

from apps.payment.providers.payze import views


urlpatterns = [
    path(
        route="payment/payze/token",
        view=views.TokenAPIView.as_view(),
        name="get-token"
    ),
    path(
        route="payment/payze/webhook/cards",
        view=views.CardsWebHooksAPIView.as_view(),
        name="cards-webhook"
    ),
    path(
        route="payment/payze/webhook/withdrawl",
        view=views.CreatePaymentAPIView.as_view(),
        name="withdrawl-webhook"
    )
]
