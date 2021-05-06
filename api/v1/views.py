from rest_framework import generics

from api.v1.serializers import RateSerializer
from rates.models import Rate


class FetchUpdateQuotes(generics.ListCreateAPIView):
    serializer_class = RateSerializer
    queryset = Rate.objects.all().order_by('-last_refreshed')
