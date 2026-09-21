
from django.db import models

#======================================================================
# Class Bank Declaration
#======================================================================
class Bank (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixName = models.CharField(max_length=200, null=True)
		$prefixLegalName = models.CharField(max_length=200, null=True)
			swiftBicValue = models.CharField(max_length=200, null=True)
	swiftBicValue = models.CharField(max_length=200, null=True)
		$prefixHeadquartersCountry = models.CharField(max_length=200, null=True)
		$prefixWebsite = models.CharField(max_length=200, null=True)
		$prefixBranches = models.ManyToManyField('Branch',  blank=True, related_name='+')
		$prefixProducts = models.ManyToManyField('BankingProduct',  blank=True, related_name='+')
		$prefixCustomers = models.ManyToManyField('Customer',  blank=True, related_name='+')
		$prefixAccounts = models.ManyToManyField('Account',  blank=True, related_name='+')
		$prefixPaymentCards = models.ManyToManyField('PaymentCard',  blank=True, related_name='+')
		$prefixLoanAccounts = models.ManyToManyField('LoanAccount',  blank=True, related_name='+')
		$prefixExchangeRates = models.ManyToManyField('ExchangeRate',  blank=True, related_name='+')
		$prefixConsents = models.ManyToManyField('Consent',  blank=True, related_name='+')
		$prefixThirdPartyProviders = models.ManyToManyField('ThirdPartyProvider',  blank=True, related_name='+')

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
		return "Bank";
    
	def objectType(self):
		return "Bank";
