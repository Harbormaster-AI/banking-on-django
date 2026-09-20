from django.urls import path


from bankingOnDjango.views import CustomerView

urlpatterns = [
    path('', CustomerView.index, name='index'),

    path('create', CustomerView.create, name='create'),
    path('update', CustomerView.update, name='update'),
    path('get', CustomerView.get, name='get'),
    path('getAll', CustomerView.getAll, name='getAll'),
    path('delete', CustomerView.delete, name='delete'),


    path('assignBank', CustomerView.assignBank, name='assignBank'),
    path('unassignBank', CustomerView.unassignBank, name='unassignBank'),




    path('addAccounts', CustomerView.addAccounts, name='addAccounts'),
    path('removeAccounts', CustomerView.removeAccounts, name='removeAccounts'),



    path('addLoanAccounts', CustomerView.addLoanAccounts, name='addLoanAccounts'),
    path('removeLoanAccounts', CustomerView.removeLoanAccounts, name='removeLoanAccounts'),



    path('addPaymentCards', CustomerView.addPaymentCards, name='addPaymentCards'),
    path('removePaymentCards', CustomerView.removePaymentCards, name='removePaymentCards'),



    path('addExternalAccounts', CustomerView.addExternalAccounts, name='addExternalAccounts'),
    path('removeExternalAccounts', CustomerView.removeExternalAccounts, name='removeExternalAccounts'),



    path('addFundsTransfers', CustomerView.addFundsTransfers, name='addFundsTransfers'),
    path('removeFundsTransfers', CustomerView.removeFundsTransfers, name='removeFundsTransfers'),



    path('addDisputes', CustomerView.addDisputes, name='addDisputes'),
    path('removeDisputes', CustomerView.removeDisputes, name='removeDisputes'),



    path('addKycProfiles', CustomerView.addKycProfiles, name='addKycProfiles'),
    path('removeKycProfiles', CustomerView.removeKycProfiles, name='removeKycProfiles'),



    path('addConsents', CustomerView.addConsents, name='addConsents'),
    path('removeConsents', CustomerView.removeConsents, name='removeConsents'),


]