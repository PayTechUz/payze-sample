"""
create payment web hook http message listener.
"""
from rest_framework import views
from rest_framework import response


class CreatePaymentAPIView(views.APIView):
    """
    create payment api view.
    """
    def post(self, request):
        """
        the post method is called
        when the payment web hook is come
        """
        print("web hook accepted")
        return response.Response()
