
from django.db import models
from bankingOnDjango.models.ConsentType import ConsentType
from bankingOnDjango.models.ConsentStatus import ConsentStatus

#======================================================================
# Class Consent Declaration
#======================================================================
#getDjangoClassDecl( $class $suffixToAdd )

#======================================================================
# attribute declarations
#======================================================================
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )
	#getDjangoAttributeDeclaration( $attribute $class $prefix )

#======================================================================
# function declarations
#======================================================================
#getDjangoToString( $class false )
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "Consent";
    
	def objectType(self):
		return "Consent";
