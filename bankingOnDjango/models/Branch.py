
from django.db import models

#======================================================================
# Class Branch Declaration
#======================================================================
class Branch (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixName = models.CharField(max_length=200, null=True)
		$prefixBranchCode = models.CharField(max_length=200, null=True)
			addressStreet = models.CharField(max_length=200, null=True)
		addressCity = models.CharField(max_length=200, null=True)
		addressState = models.CharField(max_length=200, null=True)
		addressPostalCode = models.CharField(max_length=200, null=True)
		addressCountry = models.CharField(max_length=200, null=True)
	addressCountry = models.CharField(max_length=200, null=True)
		$prefixPhone = models.CharField(max_length=200, null=True)
		$prefixOpeningHours = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixAccounts = models.ManyToManyField('Account',  blank=True, related_name='+')
		$prefixLoanAccounts = models.ManyToManyField('LoanAccount',  blank=True, related_name='+')
		$prefixAtms = models.ManyToManyField('ATM',  blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.street
		str = str + self.city
		str = str + self.state
		str = str + self.postalCode
		str = str + self.country
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Branch";
    
	def objectType(self):
		return "Branch";
