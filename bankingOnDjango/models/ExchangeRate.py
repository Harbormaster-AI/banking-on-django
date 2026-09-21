
from django.db import models

#======================================================================
# Class ExchangeRate Declaration
#======================================================================
class ExchangeRate (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixBaseCurrency = models.CharField(max_length=200, null=True)
		$prefixCounterCurrency = models.CharField(max_length=200, null=True)
		$prefixRate = models.CharField(max_length=64, null=True)
		$prefixAsOf = models.DateField(null=True)
		$prefixSource = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixFxTrades = models.ManyToManyField('FXTrade',  blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.baseCurrency
		str = str + self.counterCurrency
		str = str + self.rate
		str = str + self.asOf
		str = str + self.source
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "ExchangeRate";
    
	def objectType(self):
		return "ExchangeRate";
