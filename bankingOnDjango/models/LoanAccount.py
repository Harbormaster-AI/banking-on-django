
from django.db import models
from bankingOnDjango.models.LoanType import LoanType
from bankingOnDjango.models.RateType import RateType
from bankingOnDjango.models.InterestCompounding import InterestCompounding
from bankingOnDjango.models.LoanStatus import LoanStatus

#======================================================================
# Class LoanAccount Declaration
#======================================================================
class LoanAccount (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixLoanNumber = models.CharField(max_length=200, null=True)
			principalAmountAmount = models.CharField(max_length=64, null=True)
		principalAmountCurrency = models.CharField(max_length=200, null=True)
	principalAmountCurrency = models.CharField(max_length=200, null=True)
			outstandingPrincipalAmount = models.CharField(max_length=64, null=True)
		outstandingPrincipalCurrency = models.CharField(max_length=200, null=True)
	outstandingPrincipalCurrency = models.CharField(max_length=200, null=True)
			interestRateValue = models.CharField(max_length=64, null=True)
	interestRateValue = models.CharField(max_length=64, null=True)
		$prefixOriginationDate = models.DateField(null=True)
		$prefixMaturityDate = models.DateField(null=True)
		$prefixPaymentDayOfMonth = models.IntegerField(null=True)
		$prefixCurrency = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixBranch = models.ForeignKey('Branch', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixProduct = models.ForeignKey('BankingProduct', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixBorrowers = models.ManyToManyField('Customer',  blank=True, related_name='+')
		$prefixRepaymentSchedule = models.ManyToManyField('RepaymentSchedule',  blank=True, related_name='+')
		$prefixPayments = models.ManyToManyField('LoanPayment',  blank=True, related_name='+')
		$prefixCollateral = models.ManyToManyField('Collateral',  blank=True, related_name='+')
		$prefixFeeCharges = models.ManyToManyField('FeeCharge',  blank=True, related_name='+')
		$prefixLoanType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in LoanType])
		$prefixRateType = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in RateType])
		$prefixCompounding = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in InterestCompounding])
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in LoanStatus])

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
		return "LoanAccount";
    
	def objectType(self):
		return "LoanAccount";
