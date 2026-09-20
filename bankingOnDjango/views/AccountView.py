import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.AccountDelegate import AccountDelegate

 #======================================================================
# 
# Encapsulates data for View Account
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class AccountView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Account index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        accountId = requestData["id"]
        delegate = AccountDelegate()
        responseData = delegate.get(accountId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	account = json.loads(request.body)
	delegate = AccountDelegate()
	responseData = delegate.createFromJson( account )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	account = json.loads(request.body)
	delegate = AccountDelegate()
	responseData = delegate.save( account )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        accountId = requestData["id"]
        delegate = AccountDelegate()
        responseData = delegate.delete(accountId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = AccountDelegate()
        responseData = delegate.getAll()
        asJson = serializers.serialize("json", responseData)
        return HttpResponse(asJson, content_type="application/json");


    # ---------------------------------------------------------
    # Single association
    # ---------------------------------------------------------
    @staticmethod
    def assignBank(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.assignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBank(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.unassignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignBranch(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.assignBranch(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBranch(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.unassignBranch(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignProduct(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.assignProduct(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignProduct(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = AccountDelegate()
        responseData = delegate.unassignProduct(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
    @staticmethod
    def addOwners(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.addOwners(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeOwners(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.removeOwners(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addTransactions(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.addTransactions(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeTransactions(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.removeTransactions(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addStatements(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.addStatements(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeStatements(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.removeStatements(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addStandingInstructions(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.addStandingInstructions(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeStandingInstructions(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.removeStandingInstructions(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addFeeCharges(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.addFeeCharges(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeFeeCharges(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = AccountDelegate()
        responseData = delegate.removeFeeCharges(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


