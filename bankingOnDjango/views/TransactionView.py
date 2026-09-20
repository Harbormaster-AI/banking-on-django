import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.TransactionDelegate import TransactionDelegate

 #======================================================================
# 
# Encapsulates data for View Transaction
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class TransactionView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Transaction index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        transactionId = requestData["id"]
        delegate = TransactionDelegate()
        responseData = delegate.get(transactionId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	transaction = json.loads(request.body)
	delegate = TransactionDelegate()
	responseData = delegate.createFromJson( transaction )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	transaction = json.loads(request.body)
	delegate = TransactionDelegate()
	responseData = delegate.save( transaction )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        transactionId = requestData["id"]
        delegate = TransactionDelegate()
        responseData = delegate.delete(transactionId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = TransactionDelegate()
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
        delegate = TransactionDelegate()
        responseData = delegate.assignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignExternalCounterparty(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.assignExternalCounterparty(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignExternalCounterparty(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignExternalCounterparty(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignPaymentCard(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.assignPaymentCard(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignPaymentCard(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignPaymentCard(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignFundsTransfer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.assignFundsTransfer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignFundsTransfer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignFundsTransfer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignFxTrade(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.assignFxTrade(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignFxTrade(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignFxTrade(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignDispute(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.assignDispute(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignDispute(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = TransactionDelegate()
        responseData = delegate.unassignDispute(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
