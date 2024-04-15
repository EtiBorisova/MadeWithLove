from django.core import validators
from django.db import models

from MadeWithLove.accounts.models import MadeWithLoveUser
from MadeWithLove.ads.models import AdsModel


class Order(models.Model):
    product = models.ForeignKey(
        AdsModel,
        on_delete=models.CASCADE

    )
    city_to_delivery = models.CharField(
        max_length=30,
    )
    address_to_delivery = models.CharField(
        max_length=100,

    )
    buyer = models.ForeignKey(
        MadeWithLoveUser,
        on_delete=models.CASCADE
    )


class ReviewsModel(models.Model):
    user = models.ForeignKey(
        MadeWithLoveUser,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        AdsModel,
        on_delete=models.CASCADE
    )
    review = models.TextField()
    score = models.IntegerField(
        choices=[(v,v) for v in range(1,7)]
    )