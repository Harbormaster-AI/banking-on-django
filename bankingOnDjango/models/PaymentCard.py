
from django.db import models
from bankingOnDjango.models.CardType import CardType
from bankingOnDjango.models.CardStatus import CardStatus
from bankingOnDjango.models.CardNetwork import CardNetwork

#======================================================================
# Class PaymentCard Declaration
#======================================================================
class PaymentCard (models.Model):

#======================================================================
# attribute declarations
#======================================================================
			cardNumberValue = models.CharField(max_length=200, null=True)
	cardNumberValue = models.CharField(max_length=200, null=True)
		$prefixEmbossedName = models.CharField(max_length=200, null=True)
		$prefixExpiryMonth = models.IntegerField(null=True)
		$prefixExpiryYear = models.IntegerField(null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixCustomer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixTransactions = models.ManyToManyField('Transaction',  blank=True, related_name='+')
		$prefixCardType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in CardType])
		$prefixCardStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in CardStatus])
		$prefixNetwork = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in CardNetwork])

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
		return "PaymentCard";
    
	def objectType(self):
		return "PaymentCard";
