from rest_framework import serializers

from rates.models import Rate


class RateSerializer(serializers.ModelSerializer):
    source_currency_code = serializers.CharField(max_length=5, required=False, default='BTC')
    source_currency_name = serializers.CharField(max_length=50, required=False)
    target_currency_code = serializers.CharField(max_length=5, required=False, default='USD')
    target_currency_name = serializers.CharField(max_length=50, required=False)
    exchange_rate = serializers.FloatField(required=False)
    last_refreshed = serializers.DateTimeField(required=False)

    class Meta:
        model = Rate
        fields = (
            'source_currency_code', 'source_currency_name', 'target_currency_code', 'target_currency_name',
            'exchange_rate', 'last_refreshed'
        )

    def create(self, validated_data):
        obj = Rate.fetch_and_store_exchange_rate(
            source_currency_code=validated_data.get('source_currency_code'),
            target_currency_code=validated_data.get('target_currency_code')
        )
        return obj
