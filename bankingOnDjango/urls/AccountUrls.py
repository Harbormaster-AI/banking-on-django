from django.urls import path


from bankingOnDjango.views import AccountView

urlpatterns = [
    path('', AccountView.index, name='index'),

    path('create', AccountView.create, name='create'),
    path('update', AccountView.update, name='update'),
    path('get', AccountView.get, name='get'),
    path('getAll', AccountView.getAll, name='getAll'),
    path('delete', AccountView.delete, name='delete'),


    path('assignBank', AccountView.assignBank, name='assignBank'),
    path('unassignBank', AccountView.unassignBank, name='unassignBank'),



    path('assignBranch', AccountView.assignBranch, name='assignBranch'),
    path('unassignBranch', AccountView.unassignBranch, name='unassignBranch'),



    path('assignProduct', AccountView.assignProduct, name='assignProduct'),
    path('unassignProduct', AccountView.unassignProduct, name='unassignProduct'),




    path('addOwners', AccountView.addOwners, name='addOwners'),
    path('removeOwners', AccountView.removeOwners, name='removeOwners'),



    path('addTransactions', AccountView.addTransactions, name='addTransactions'),
    path('removeTransactions', AccountView.removeTransactions, name='removeTransactions'),



    path('addStatements', AccountView.addStatements, name='addStatements'),
    path('removeStatements', AccountView.removeStatements, name='removeStatements'),



    path('addStandingInstructions', AccountView.addStandingInstructions, name='addStandingInstructions'),
    path('removeStandingInstructions', AccountView.removeStandingInstructions, name='removeStandingInstructions'),



    path('addFeeCharges', AccountView.addFeeCharges, name='addFeeCharges'),
    path('removeFeeCharges', AccountView.removeFeeCharges, name='removeFeeCharges'),


]