from django.db import DatabaseError

from apps.card.models.payment import PaymentID
from apps.card.models.card import PayzeCardModel

from apps.utility.logger import logger
from apps.utility.exceptions import ServiceAPIException
from apps.utility.exceptions import ServiceAPIException500


class CardProcessor:

    def add_payment(self, payment_id: str) -> None:
        try:
            PaymentID.objects.get_or_create(
                PID=payment_id
            )

        except DatabaseError as error:
            logger.error("Error was occurred while creating payment: %s", error)
            raise ServiceAPIException500()

    def set_captured(
        self, 
        payment_id: str,
        card_mask: str,
        card_holder: str,
        expire_date: str,
        card_brand: str
    ) -> None:
        try:
            card = PayzeCardModel.objects.get(
                payment_id=PaymentID.objects.get(
                    PID=payment_id
                )
            )

            if card is not None:
                card.card_mask = card_mask
                card.card_holder = card_holder
                card.expire_date = expire_date
                card.card_brand = card_brand
                card.save()

        except PayzeCardModel.DoesNotExist as error:
            logger.info("PayzeCardModel DoesNotExist started creating - %s" % error)
            PayzeCardModel.objects.create(
                payment_id=PaymentID.objects.get(
                    PID=payment_id
                ),
                status=False,
                card_mask=card_mask,
                card_holder=card_holder,
                expire_date=expire_date,
                card_brand=card_brand
            )

        except PaymentID.DoesNotExist as error:
            logger.error("Error was occurred while set_captured: %s", error)
            raise ServiceAPIException(
                type="not_found",
                status_code=404,
                message="payment id was not found"
            )
        

        except PayzeCardModel.DoesNotExist as error:
            logger.error("Error was occurred while set captured: %s", error)
            raise ServiceAPIException(
                type="not_found",
                status_code=404,
                message="payment id was not found"
            )

        except DatabaseError as error:
            logger.error("Error was occurred while set captured: %s", error)
            raise ServiceAPIException500()


    def set_to_activated(
        self,
        payment_id: str
    ) -> None:

        try:
            card = PayzeCardModel.objects.filter(
                payment_id=PaymentID.objects.get(
                    PID=payment_id
                ),
                status=False
            ).last()
            card.status = True
            card.save()

        except PaymentID.DoesNotExist as error:
            logger.error("Error was occurred while set_to_activated: %s", error)
            raise ServiceAPIException(
                type="not_found",
                status_code=404,
                message="payment id was not found"
            )

        except DatabaseError as error:
            logger.error("Error was occurred while set_to_activated: %s", error)
            raise ServiceAPIException()

        except AttributeError as error:
            logger.error("Error was occurred while set_to_activated: %s", error)
            raise ServiceAPIException(
                type="not_found",
                status_code=404,
                message="card was not found"
            )

    def set_token(self, payment_id, card_token) -> None:
        try:
            card = PayzeCardModel.objects.get(
                payment_id=PaymentID.objects.get(
                    PID=payment_id
                )
            )
            card.card_token = card_token
            card.save()

        except PaymentID.DoesNotExist as error:
            logger.error("error was occurred while getting payment id: %s", error)
            raise ServiceAPIException(
                type="not_found",
                message="payment id not found",
                status_code=404
            )

        except PayzeCardModel.DoesNotExist as error:
            PayzeCardModel.objects.create(
                payment_id=PaymentID.objects.get(
                    PID=payment_id
                ),
                card_token=card_token
            )

        except DatabaseError as error:
            logger.error("Error was occurred while set_token: %s", error)
            raise ServiceAPIException500()

        except AttributeError as error:
            logger.error("Error was occurred while set_token: %s", error)
            raise ServiceAPIException(
                type="not_found",
                status_code=404,
                message="card was not found"
            )


card_processor = CardProcessor()
