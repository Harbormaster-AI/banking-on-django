
from django.db import models

#======================================================================
# Class ExternalAccount Declaration
#======================================================================
class ExternalAccount (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixName = models.CharField(max_length=200, null=True)
			ibanValue = models.CharField(max_length=200, null=True)
	ibanValue = models.CharField(max_length=200, null=True)
			accountNumberValue = models.CharField(max_length=200, null=True)
	accountNumberValue = models.CharField(max_length=200, null=True)
			bicValue = models.CharField(max_length=200, null=True)
	bicValue = models.CharField(max_length=200, null=True)
		$prefixBankName = models.CharField(max_length=200, null=True)
		$prefixCountry = models.CharField(max_length=200, null=True)
		$prefixCustomer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixTransactions = models.ManyToManyField('Transaction',  blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.value
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "ExternalAccount";
    
	def objectType(self):
		return "ExternalAccount";
