

from django.db import models

from MadeWithLove.accounts.models import MadeWithLoveUser


class AdsModel(models.Model):

    product_name = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    time_for_production_in_days = models.IntegerField()
    ads_image = models.ImageField()
    price = models.FloatField()
    seller = models.ForeignKey(
        MadeWithLoveUser,
        on_delete=models.CASCADE,
    )

