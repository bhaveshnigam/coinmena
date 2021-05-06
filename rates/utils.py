import datetime

from alpha_vantage.foreignexchange import ForeignExchange

from django.conf import settings


def get_exchange_rates(from_currency, to_currency):
    cc = ForeignExchange(key=settings.ALPHA_VANTAGE_API_KEY)
    data, _ = cc.get_currency_exchange_rate(from_currency=from_currency, to_currency=to_currency)
    reformatted_data = {
        'source_currency_code': data['1. From_Currency Code'],
        'source_currency_name': data['2. From_Currency Name'],
        'target_currency_code': data['3. To_Currency Code'],
        'target_currency_name': data['4. To_Currency Name'],
        'exchange_rate': data['5. Exchange Rate'],
        'last_refreshed': datetime.datetime.strptime(data['6. Last Refreshed'], '%Y-%m-%d %H:%M:%S')
    }
    return reformatted_data
