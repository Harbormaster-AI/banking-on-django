
from django.db import models
from bankingOnDjango.models.CardType import CardType
from bankingOnDjango.models.CardStatus import CardStatus
from bankingOnDjango.models.CardNetwork import CardNetwork

#======================================================================
# Class PaymentCard Declaration
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
		return "PaymentCard";
    
	def objectType(self):
		return "PaymentCard";
