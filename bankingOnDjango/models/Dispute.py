
from django.db import models
from bankingOnDjango.models.DisputeStatus import DisputeStatus

#======================================================================
# Class Dispute Declaration
#======================================================================
class Dispute (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixDisputeReference = models.CharField(max_length=200, null=True)
		$prefixRaisedOn = models.DateField(null=True)
		$prefixReason = models.CharField(max_length=200, null=True)
		$prefixTransaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixCustomer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixPaymentCard = models.ForeignKey('PaymentCard', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in DisputeStatus])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.disputeReference
		str = str + self.raisedOn
		str = str + self.reason
		str = str + self.status
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Dispute";
    
	def objectType(self):
		return "Dispute";
