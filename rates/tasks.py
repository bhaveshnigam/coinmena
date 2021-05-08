from coinmena import celery_app
from rates.models import Rate


@celery_app.task()
def fetch_latest_rate_btc_to_usd():
    Rate.fetch_and_store_exchange_rate('BTC', 'USD')
