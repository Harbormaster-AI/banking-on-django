
from django.db import models
from bankingOnDjango.models.ScreeningOutcome import ScreeningOutcome

#======================================================================
# Class ScreeningResult Declaration
#======================================================================
#getDjangoClassDecl( $class $suffixToAdd )

#======================================================================
# attribute declarations
#======================================================================
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
		return "ScreeningResult";
    
	def objectType(self):
		return "ScreeningResult";
