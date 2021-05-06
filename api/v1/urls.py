from django.urls import path, include

from api.v1.views import FetchUpdateQuotes

urlpatterns = [
    path('quotes', FetchUpdateQuotes.as_view(), name='fetch-update-quotes')
]
