
from django.db import models
from bankingOnDjango.models.RiskRating import RiskRating

#======================================================================
# Class RiskAssessment Declaration
#======================================================================
class RiskAssessment (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixScore = models.IntegerField(null=True)
		$prefixAssessedOn = models.DateField(null=True)
		$prefixKycProfile = models.ForeignKey('KycProfile', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixRating = models.CharField(max_length=64, null=True, choices=[(tag.name, tag.value) for tag in RiskRating])

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.score
		str = str + self.assessedOn
		str = str + self.rating
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "RiskAssessment";
    
	def objectType(self):
		return "RiskAssessment";
