
from django.db import models
from bankingOnDjango.models.TradeStatus import TradeStatus

#======================================================================
# Class FXTrade Declaration
#======================================================================
class FXTrade (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixTradeReference = models.CharField(max_length=200, null=True)
		$prefixTradeDate = models.DateField(null=True)
		$prefixSettlementDate = models.DateField(null=True)
			amountSoldAmount = models.CharField(max_length=64, null=True)
		amountSoldCurrency = models.CharField(max_length=200, null=True)
	amountSoldCurrency = models.CharField(max_length=200, null=True)
			amountBoughtAmount = models.CharField(max_length=64, null=True)
		amountBoughtCurrency = models.CharField(max_length=200, null=True)
	amountBoughtCurrency = models.CharField(max_length=200, null=True)
		$prefixRate = models.CharField(max_length=64, null=True)
		$prefixCustomer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixExchangeRate = models.ForeignKey('ExchangeRate', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixSourceAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixDestinationAccount = models.ForeignKey('Account', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixTransaction = models.OneToOneField('Transaction', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in TradeStatus])

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
		return "FXTrade";
    
	def objectType(self):
		return "FXTrade";
