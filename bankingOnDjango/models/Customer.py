
from django.db import models
from bankingOnDjango.models.CustomerType import CustomerType
from bankingOnDjango.models.RiskRating import RiskRating
from bankingOnDjango.models.KycStatus import KycStatus

#======================================================================
# Class Customer Declaration
#======================================================================
class Customer (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixFirstName = models.CharField(max_length=200, null=True)
		$prefixLastName = models.CharField(max_length=200, null=True)
		$prefixLegalName = models.CharField(max_length=200, null=True)
		$prefixDateOfBirth = models.DateField(null=True)
		$prefixTaxId = models.CharField(max_length=200, null=True)
		$prefixEmail = models.CharField(max_length=200, null=True)
		$prefixPhone = models.CharField(max_length=200, null=True)
			addressStreet = models.CharField(max_length=200, null=True)
		addressCity = models.CharField(max_length=200, null=True)
		addressState = models.CharField(max_length=200, null=True)
		addressPostalCode = models.CharField(max_length=200, null=True)
		addressCountry = models.CharField(max_length=200, null=True)
	addressCountry = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixAccounts = models.ManyToManyField('Account',  blank=True, related_name='+')
		$prefixLoanAccounts = models.ManyToManyField('LoanAccount',  blank=True, related_name='+')
		$prefixPaymentCards = models.ManyToManyField('PaymentCard',  blank=True, related_name='+')
		$prefixExternalAccounts = models.ManyToManyField('ExternalAccount',  blank=True, related_name='+')
		$prefixFundsTransfers = models.ManyToManyField('FundsTransfer',  blank=True, related_name='+')
		$prefixDisputes = models.ManyToManyField('Dispute',  blank=True, related_name='+')
		$prefixKycProfiles = models.ManyToManyField('KycProfile',  blank=True, related_name='+')
		$prefixConsents = models.ManyToManyField('Consent',  blank=True, related_name='+')
		$prefixCustomerType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in CustomerType])
		$prefixRiskRating = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in RiskRating])
		$prefixKycStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in KycStatus])

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
		return "Customer";
    
	def objectType(self):
		return "Customer";
