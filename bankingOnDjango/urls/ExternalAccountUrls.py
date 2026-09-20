from django.urls import path


from bankingOnDjango.views import ExternalAccountView

urlpatterns = [
    path('', ExternalAccountView.index, name='index'),

    path('create', ExternalAccountView.create, name='create'),
    path('update', ExternalAccountView.update, name='update'),
    path('get', ExternalAccountView.get, name='get'),
    path('getAll', ExternalAccountView.getAll, name='getAll'),
    path('delete', ExternalAccountView.delete, name='delete'),


    path('assignCustomer', ExternalAccountView.assignCustomer, name='assignCustomer'),
    path('unassignCustomer', ExternalAccountView.unassignCustomer, name='unassignCustomer'),




    path('addTransactions', ExternalAccountView.addTransactions, name='addTransactions'),
    path('removeTransactions', ExternalAccountView.removeTransactions, name='removeTransactions'),


]