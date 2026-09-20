from django.urls import path


from bankingOnDjango.views import BankingProductView

urlpatterns = [
    path('', BankingProductView.index, name='index'),

    path('create', BankingProductView.create, name='create'),
    path('update', BankingProductView.update, name='update'),
    path('get', BankingProductView.get, name='get'),
    path('getAll', BankingProductView.getAll, name='getAll'),
    path('delete', BankingProductView.delete, name='delete'),


    path('assignBank', BankingProductView.assignBank, name='assignBank'),
    path('unassignBank', BankingProductView.unassignBank, name='unassignBank'),




    path('addAccounts', BankingProductView.addAccounts, name='addAccounts'),
    path('removeAccounts', BankingProductView.removeAccounts, name='removeAccounts'),



    path('addLoanAccounts', BankingProductView.addLoanAccounts, name='addLoanAccounts'),
    path('removeLoanAccounts', BankingProductView.removeLoanAccounts, name='removeLoanAccounts'),



    path('addPaymentCards', BankingProductView.addPaymentCards, name='addPaymentCards'),
    path('removePaymentCards', BankingProductView.removePaymentCards, name='removePaymentCards'),


]