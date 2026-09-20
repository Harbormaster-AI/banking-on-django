import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.FXTradeDelegate import FXTradeDelegate

 #======================================================================
# 
# Encapsulates data for View FXTrade
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class FXTradeView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the FXTrade index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        fXTradeId = requestData["id"]
        delegate = FXTradeDelegate()
        responseData = delegate.get(fXTradeId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	fXTrade = json.loads(request.body)
	delegate = FXTradeDelegate()
	responseData = delegate.createFromJson( fXTrade )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	fXTrade = json.loads(request.body)
	delegate = FXTradeDelegate()
	responseData = delegate.save( fXTrade )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        fXTradeId = requestData["id"]
        delegate = FXTradeDelegate()
        responseData = delegate.delete(fXTradeId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = FXTradeDelegate()
        responseData = delegate.getAll()
        asJson = serializers.serialize("json", responseData)
        return HttpResponse(asJson, content_type="application/json");


    # ---------------------------------------------------------
    # Single association
    # ---------------------------------------------------------
    @staticmethod
    def assignCustomer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignCustomer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignCustomer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignCustomer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignBank(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBank(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignExchangeRate(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignExchangeRate(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignExchangeRate(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignExchangeRate(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignSourceAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignSourceAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignSourceAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignSourceAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignDestinationAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignDestinationAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignDestinationAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignDestinationAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignTransaction(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.assignTransaction(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignTransaction(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = FXTradeDelegate()
        responseData = delegate.unassignTransaction(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
