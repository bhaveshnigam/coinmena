from django.db import models

from rates.utils import get_exchange_rates


class Rate(models.Model):
    source_currency_code = models.CharField(max_length=5)
    source_currency_name = models.CharField(max_length=50)
    target_currency_code = models.CharField(max_length=5)
    target_currency_name = models.CharField(max_length=50)
    exchange_rate = models.FloatField()
    last_refreshed = models.DateTimeField()

    def __str__(self):
        return '%s - %s: %s' % (self.source_currency_code, self.target_currency_code, self.exchange_rate)

    @classmethod
    def fetch_and_store_exchange_rate(cls, source_currency_code, target_currency_code):
        exchange_data = get_exchange_rates(source_currency_code, target_currency_code)
        rate_obj = cls.objects.create(
            source_currency_code=exchange_data['source_currency_code'],
            source_currency_name=exchange_data['source_currency_name'],
            target_currency_code=exchange_data['target_currency_code'],
            target_currency_name=exchange_data['target_currency_name'],
            exchange_rate=exchange_data['exchange_rate'],
            last_refreshed=exchange_data['last_refreshed'],
        )
        return rate_obj
