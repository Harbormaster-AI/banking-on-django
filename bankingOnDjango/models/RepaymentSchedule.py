
from django.db import models
from bankingOnDjango.models.InstallmentStatus import InstallmentStatus

#======================================================================
# Class RepaymentSchedule Declaration
#======================================================================
class RepaymentSchedule (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixInstallmentNumber = models.IntegerField(null=True)
		$prefixDueDate = models.DateField(null=True)
			principalDueAmount = models.CharField(max_length=64, null=True)
		principalDueCurrency = models.CharField(max_length=200, null=True)
	principalDueCurrency = models.CharField(max_length=200, null=True)
			interestDueAmount = models.CharField(max_length=64, null=True)
		interestDueCurrency = models.CharField(max_length=200, null=True)
	interestDueCurrency = models.CharField(max_length=200, null=True)
			totalDueAmount = models.CharField(max_length=64, null=True)
		totalDueCurrency = models.CharField(max_length=200, null=True)
	totalDueCurrency = models.CharField(max_length=200, null=True)
		$prefixLoanAccount = models.ForeignKey('LoanAccount', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixPayment = models.ForeignKey('LoanPayment', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in InstallmentStatus])

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
		return "RepaymentSchedule";
    
	def objectType(self):
		return "RepaymentSchedule";
