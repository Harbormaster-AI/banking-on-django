import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.StandingInstructionDelegate import StandingInstructionDelegate

 #======================================================================
# 
# Encapsulates data for View StandingInstruction
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class StandingInstructionView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the StandingInstruction index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        standingInstructionId = requestData["id"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.get(standingInstructionId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	standingInstruction = json.loads(request.body)
	delegate = StandingInstructionDelegate()
	responseData = delegate.createFromJson( standingInstruction )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	standingInstruction = json.loads(request.body)
	delegate = StandingInstructionDelegate()
	responseData = delegate.save( standingInstruction )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        standingInstructionId = requestData["id"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.delete(standingInstructionId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = StandingInstructionDelegate()
        responseData = delegate.getAll()
        asJson = serializers.serialize("json", responseData)
        return HttpResponse(asJson, content_type="application/json");


    # ---------------------------------------------------------
    # Single association
    # ---------------------------------------------------------
    @staticmethod
    def assignAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.assignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.unassignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignBeneficiary(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.assignBeneficiary(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBeneficiary(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = StandingInstructionDelegate()
        responseData = delegate.unassignBeneficiary(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
