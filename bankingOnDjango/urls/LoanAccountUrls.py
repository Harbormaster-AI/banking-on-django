from django.urls import path


from bankingOnDjango.views import LoanAccountView

urlpatterns = [
    path('', LoanAccountView.index, name='index'),

    path('create', LoanAccountView.create, name='create'),
    path('update', LoanAccountView.update, name='update'),
    path('get', LoanAccountView.get, name='get'),
    path('getAll', LoanAccountView.getAll, name='getAll'),
    path('delete', LoanAccountView.delete, name='delete'),


    path('assignBank', LoanAccountView.assignBank, name='assignBank'),
    path('unassignBank', LoanAccountView.unassignBank, name='unassignBank'),



    path('assignBranch', LoanAccountView.assignBranch, name='assignBranch'),
    path('unassignBranch', LoanAccountView.unassignBranch, name='unassignBranch'),



    path('assignProduct', LoanAccountView.assignProduct, name='assignProduct'),
    path('unassignProduct', LoanAccountView.unassignProduct, name='unassignProduct'),




    path('addBorrowers', LoanAccountView.addBorrowers, name='addBorrowers'),
    path('removeBorrowers', LoanAccountView.removeBorrowers, name='removeBorrowers'),



    path('addRepaymentSchedule', LoanAccountView.addRepaymentSchedule, name='addRepaymentSchedule'),
    path('removeRepaymentSchedule', LoanAccountView.removeRepaymentSchedule, name='removeRepaymentSchedule'),



    path('addPayments', LoanAccountView.addPayments, name='addPayments'),
    path('removePayments', LoanAccountView.removePayments, name='removePayments'),



    path('addCollateral', LoanAccountView.addCollateral, name='addCollateral'),
    path('removeCollateral', LoanAccountView.removeCollateral, name='removeCollateral'),



    path('addFeeCharges', LoanAccountView.addFeeCharges, name='addFeeCharges'),
    path('removeFeeCharges', LoanAccountView.removeFeeCharges, name='removeFeeCharges'),


]