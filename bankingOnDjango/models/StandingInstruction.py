
from django.db import models
from bankingOnDjango.models.StandingInstructionFrequency import StandingInstructionFrequency
from bankingOnDjango.models.StandingInstructionStatus import StandingInstructionStatus

#======================================================================
# Class StandingInstruction Declaration
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

#======================================================================
# function declarations
#======================================================================
#getDjangoToString( $class false )
    
	def __str__(self):
		return self.toString();

	def identity(self):
		return "StandingInstruction";
    
	def objectType(self):
		return "StandingInstruction";
