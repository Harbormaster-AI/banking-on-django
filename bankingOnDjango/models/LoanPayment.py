
from django.db import models
from bankingOnDjango.models.PaymentMethod import PaymentMethod
from bankingOnDjango.models.PaymentStatus import PaymentStatus

#======================================================================
# Class LoanPayment Declaration
#======================================================================
class LoanPayment (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixPaymentReference = models.CharField(max_length=200, null=True)
			amountAmount = models.CharField(max_length=64, null=True)
		amountCurrency = models.CharField(max_length=200, null=True)
	amountCurrency = models.CharField(max_length=200, null=True)
		$prefixPaymentDate = models.DateField(null=True)
		$prefixLoanAccount = models.ForeignKey('LoanAccount', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixTransaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
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
		return "LoanPayment";
    
	def objectType(self):
		return "LoanPayment";
