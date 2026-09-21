
from django.db import models

#======================================================================
# Class ThirdPartyProvider Declaration
#======================================================================
class ThirdPartyProvider (models.Model):

#======================================================================
# attribute declarations
#======================================================================
		$prefixName = models.CharField(max_length=200, null=True)
		$prefixRegistrationId = models.CharField(max_length=200, null=True)
		$prefixWebsite = models.CharField(max_length=200, null=True)
		$prefixBank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
		$prefixConsents = models.ManyToManyField('Consent',  blank=True, related_name='+')

#======================================================================
# function declarations
#======================================================================
	def toString(self):
		str = ""
		str = str + self.name
		str = str + self.registrationId
		str = str + self.website
		return str;
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "ThirdPartyProvider";
    
	def objectType(self):
		return "ThirdPartyProvider";
