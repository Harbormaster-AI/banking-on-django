
from django.db import models
from bankingOnDjango.models.FeeType import FeeType

#======================================================================
# Class FeeCharge Declaration
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

#======================================================================
# function declarations
#======================================================================
#getDjangoToString( $class false )
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "FeeCharge";
    
	def objectType(self):
		return "FeeCharge";
