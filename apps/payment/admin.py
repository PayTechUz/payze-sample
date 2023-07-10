from django.contrib import admin

from apps.payment.models.transactions import Transactions

admin.site.register(Transactions)
