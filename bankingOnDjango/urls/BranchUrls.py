from django.urls import path


from bankingOnDjango.views import BranchView

urlpatterns = [
    path('', BranchView.index, name='index'),

    path('create', BranchView.create, name='create'),
    path('update', BranchView.update, name='update'),
    path('get', BranchView.get, name='get'),
    path('getAll', BranchView.getAll, name='getAll'),
    path('delete', BranchView.delete, name='delete'),


    path('assignBank', BranchView.assignBank, name='assignBank'),
    path('unassignBank', BranchView.unassignBank, name='unassignBank'),




    path('addAccounts', BranchView.addAccounts, name='addAccounts'),
    path('removeAccounts', BranchView.removeAccounts, name='removeAccounts'),



    path('addLoanAccounts', BranchView.addLoanAccounts, name='addLoanAccounts'),
    path('removeLoanAccounts', BranchView.removeLoanAccounts, name='removeLoanAccounts'),



    path('addAtms', BranchView.addAtms, name='addAtms'),
    path('removeAtms', BranchView.removeAtms, name='removeAtms'),


]