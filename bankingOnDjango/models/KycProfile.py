
from django.db import models
from bankingOnDjango.models.KycStatus import KycStatus

#======================================================================
# Class KycProfile Declaration
#======================================================================
class KycProfile (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixProfileId = models.CharField(max_length=200, null=True)
		$prefixLastReviewedOn = models.DateField(null=True)
		$prefixCustomer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixIdentityDocuments = models.ManyToManyField('IdentityDocument',  blank=True, related_name='+')
		$prefixRiskAssessments = models.ManyToManyField('RiskAssessment',  blank=True, related_name='+')
		$prefixScreenings = models.ManyToManyField('ScreeningResult',  blank=True, related_name='+')
		$prefixStatus = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in KycStatus])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.profileId
		str = str + self.lastReviewedOn
		str = str + self.status
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "KycProfile";
    
	def objectType(self):
		return "KycProfile";
