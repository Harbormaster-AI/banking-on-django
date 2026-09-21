
from django.db import models
from bankingOnDjango.models.AccountType import AccountType
from bankingOnDjango.models.AccountOwnershipType import AccountOwnershipType
from bankingOnDjango.models.AccountStatus import AccountStatus

#======================================================================
# Class Account Declaration
#======================================================================
class Account (models.Model):

#======================================================================
# attribute declarations
#======================================================================
			accountNumberValue = models.CharField(max_length=200, null=True)
	accountNumberValue = models.CharField(max_length=200, null=True)
			ibanValue = models.CharField(max_length=200, null=True)
	ibanValue = models.CharField(max_length=200, null=True)
		$prefixAccountName = models.CharField(max_length=200, null=True)
		$prefixCurrency = models.CharField(max_length=200, null=True)
		$prefixOpenedOn = models.DateField(null=True)
		$prefixClosedOn = models.DateField(null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixBranch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixProduct = models.ForeignKey('BankingProduct', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixOwners = models.ManyToManyField('Customer',  blank=True, related_name='+')
		$prefixTransactions = models.ManyToManyField('Transaction',  blank=True, related_name='+')
		$prefixStatements = models.ManyToManyField('AccountStatement',  blank=True, related_name='+')
		$prefixStandingInstructions = models.ManyToManyField('StandingInstruction',  blank=True, related_name='+')
		$prefixFeeCharges = models.ManyToManyField('FeeCharge',  blank=True, related_name='+')
		$prefixAccountType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in AccountType])
		$prefixOwnershipType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in AccountOwnershipType])
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in AccountStatus])

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
		return "Account";
    
	def objectType(self):
		return "Account";
