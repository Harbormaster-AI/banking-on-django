from django.urls import path


from bankingOnDjango.views import BankView

urlpatterns = [
    path('', BankView.index, name='index'),

    path('create', BankView.create, name='create'),
    path('update', BankView.update, name='update'),
    path('get', BankView.get, name='get'),
    path('getAll', BankView.getAll, name='getAll'),
    path('delete', BankView.delete, name='delete'),



    path('addBranches', BankView.addBranches, name='addBranches'),
    path('removeBranches', BankView.removeBranches, name='removeBranches'),



    path('addProducts', BankView.addProducts, name='addProducts'),
    path('removeProducts', BankView.removeProducts, name='removeProducts'),



    path('addCustomers', BankView.addCustomers, name='addCustomers'),
    path('removeCustomers', BankView.removeCustomers, name='removeCustomers'),



    path('addAccounts', BankView.addAccounts, name='addAccounts'),
    path('removeAccounts', BankView.removeAccounts, name='removeAccounts'),



    path('addPaymentCards', BankView.addPaymentCards, name='addPaymentCards'),
    path('removePaymentCards', BankView.removePaymentCards, name='removePaymentCards'),



    path('addLoanAccounts', BankView.addLoanAccounts, name='addLoanAccounts'),
    path('removeLoanAccounts', BankView.removeLoanAccounts, name='removeLoanAccounts'),



    path('addExchangeRates', BankView.addExchangeRates, name='addExchangeRates'),
    path('removeExchangeRates', BankView.removeExchangeRates, name='removeExchangeRates'),



    path('addConsents', BankView.addConsents, name='addConsents'),
    path('removeConsents', BankView.removeConsents, name='removeConsents'),



    path('addThirdPartyProviders', BankView.addThirdPartyProviders, name='addThirdPartyProviders'),
    path('removeThirdPartyProviders', BankView.removeThirdPartyProviders, name='removeThirdPartyProviders'),


]