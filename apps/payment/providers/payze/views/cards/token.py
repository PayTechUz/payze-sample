"""
token views
"""
from rest_framework import views
from rest_framework import response

from apps.abc.app import IApp
from apps.app import app_context

from apps.payment.providers.payze.params.response \
    import GetToken as GT


class TokenAPIView(views.APIView):
    """
    token api view for getting tokens
    and activating the cards.
    """
    # pylint: disable=W0613
    def get(self, request, context: IApp = app_context):
        """
        the get method for getting draft tokens.
        """
        data: GT = context.get_token()

        return response.Response({
            "payment_url": str(data.data.payment.payment_url),
            "token": data.data.payment.card_payment.token
        })
