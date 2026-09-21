
from django.db import models
from bankingOnDjango.models.StatementDeliveryMethod import StatementDeliveryMethod

#======================================================================
# Class AccountStatement Declaration
#======================================================================
class AccountStatement (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixStatementNumber = models.CharField(max_length=200, null=True)
		$prefixPeriodStart = models.DateField(null=True)
		$prefixPeriodEnd = models.DateField(null=True)
			openingBalanceAmount = models.CharField(max_length=64, null=True)
		openingBalanceCurrency = models.CharField(max_length=200, null=True)
	openingBalanceCurrency = models.CharField(max_length=200, null=True)
			closingBalanceAmount = models.CharField(max_length=64, null=True)
		closingBalanceCurrency = models.CharField(max_length=200, null=True)
	closingBalanceCurrency = models.CharField(max_length=200, null=True)
		$prefixAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixDeliveryMethod = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in StatementDeliveryMethod])

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
		return "AccountStatement";
    
	def objectType(self):
		return "AccountStatement";
