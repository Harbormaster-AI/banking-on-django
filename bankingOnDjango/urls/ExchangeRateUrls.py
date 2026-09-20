from django.urls import path


from bankingOnDjango.views import ExchangeRateView

urlpatterns = [
    path('', ExchangeRateView.index, name='index'),

    path('create', ExchangeRateView.create, name='create'),
    path('update', ExchangeRateView.update, name='update'),
    path('get', ExchangeRateView.get, name='get'),
    path('getAll', ExchangeRateView.getAll, name='getAll'),
    path('delete', ExchangeRateView.delete, name='delete'),


    path('assignBank', ExchangeRateView.assignBank, name='assignBank'),
    path('unassignBank', ExchangeRateView.unassignBank, name='unassignBank'),




    path('addFxTrades', ExchangeRateView.addFxTrades, name='addFxTrades'),
    path('removeFxTrades', ExchangeRateView.removeFxTrades, name='removeFxTrades'),


]