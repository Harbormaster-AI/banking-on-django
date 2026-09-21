
from django.db import models
from bankingOnDjango.models.PaymentMethod import PaymentMethod
from bankingOnDjango.models.PaymentStatus import PaymentStatus

#======================================================================
# Class FundsTransfer Declaration
#======================================================================
class FundsTransfer (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixTransferReference = models.CharField(max_length=200, null=True)
			amountAmount = models.CharField(max_length=64, null=True)
		amountCurrency = models.CharField(max_length=200, null=True)
	amountCurrency = models.CharField(max_length=200, null=True)
		$prefixRequestedDate = models.DateField(null=True)
		$prefixExecutionDate = models.DateField(null=True)
		$prefixPurpose = models.CharField(max_length=200, null=True)
			feeAmountAmount = models.CharField(max_length=64, null=True)
		feeAmountCurrency = models.CharField(max_length=200, null=True)
	feeAmountCurrency = models.CharField(max_length=200, null=True)
		$prefixSourceAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixDestinationAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixExternalBeneficiary = models.ForeignKey('ExternalAccount', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixInitiatedBy = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixTransactions = models.ManyToManyField('Transaction',  blank=True, related_name='+')
		$prefixMethod = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in PaymentMethod])
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in PaymentStatus])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.amount
		str = str + self.currency
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "FundsTransfer";
    
	def objectType(self):
		return "FundsTransfer";
