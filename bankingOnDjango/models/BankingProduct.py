
from django.db import models
from bankingOnDjango.models.ProductCategory import ProductCategory

#======================================================================
# Class BankingProduct Declaration
#======================================================================
class BankingProduct (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixProductCode = models.CharField(max_length=200, null=True)
		$prefixName = models.CharField(max_length=200, null=True)
		$prefixDescription = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixAccounts = models.ManyToManyField('Account',  blank=True, related_name='+')
		$prefixLoanAccounts = models.ManyToManyField('LoanAccount',  blank=True, related_name='+')
		$prefixPaymentCards = models.ManyToManyField('PaymentCard',  blank=True, related_name='+')
		$prefixProductCategory = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in ProductCategory])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.productCode
		str = str + self.name
		str = str + self.description
		str = str + self.productCategory
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "BankingProduct";
    
	def objectType(self):
		return "BankingProduct";
