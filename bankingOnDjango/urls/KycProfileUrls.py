from django.urls import path


from bankingOnDjango.views import KycProfileView

urlpatterns = [
    path('', KycProfileView.index, name='index'),

    path('create', KycProfileView.create, name='create'),
    path('update', KycProfileView.update, name='update'),
    path('get', KycProfileView.get, name='get'),
    path('getAll', KycProfileView.getAll, name='getAll'),
    path('delete', KycProfileView.delete, name='delete'),


    path('assignCustomer', KycProfileView.assignCustomer, name='assignCustomer'),
    path('unassignCustomer', KycProfileView.unassignCustomer, name='unassignCustomer'),




    path('addIdentityDocuments', KycProfileView.addIdentityDocuments, name='addIdentityDocuments'),
    path('removeIdentityDocuments', KycProfileView.removeIdentityDocuments, name='removeIdentityDocuments'),



    path('addRiskAssessments', KycProfileView.addRiskAssessments, name='addRiskAssessments'),
    path('removeRiskAssessments', KycProfileView.removeRiskAssessments, name='removeRiskAssessments'),



    path('addScreenings', KycProfileView.addScreenings, name='addScreenings'),
    path('removeScreenings', KycProfileView.removeScreenings, name='removeScreenings'),


]