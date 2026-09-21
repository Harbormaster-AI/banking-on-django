
from django.db import models
from bankingOnDjango.models.TransactionDirection import TransactionDirection
from bankingOnDjango.models.TransactionType import TransactionType
from bankingOnDjango.models.TransactionStatus import TransactionStatus
from bankingOnDjango.models.ChannelType import ChannelType

#======================================================================
# Class Transaction Declaration
#======================================================================
class Transaction (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixBookingDate = models.DateField(null=True)
		$prefixValueDate = models.DateField(null=True)
			amountAmount = models.CharField(max_length=64, null=True)
		amountCurrency = models.CharField(max_length=200, null=True)
	amountCurrency = models.CharField(max_length=200, null=True)
		$prefixDescription = models.CharField(max_length=200, null=True)
		$prefixAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixExternalCounterparty = models.ForeignKey('ExternalAccount', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixPaymentCard = models.ForeignKey('PaymentCard', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixFundsTransfer = models.ForeignKey('FundsTransfer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixFxTrade = models.ForeignKey('FXTrade', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixDispute = models.OneToOneField('Dispute', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixDirection = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in TransactionDirection])
		$prefixTransactionType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in TransactionType])
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in TransactionStatus])
		$prefixChannel = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in ChannelType])

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
		return "Transaction";
    
	def objectType(self):
		return "Transaction";
