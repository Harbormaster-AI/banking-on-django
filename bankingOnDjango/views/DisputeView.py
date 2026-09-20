import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.DisputeDelegate import DisputeDelegate

 #======================================================================
# 
# Encapsulates data for View Dispute
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class DisputeView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the Dispute index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        disputeId = requestData["id"]
        delegate = DisputeDelegate()
        responseData = delegate.get(disputeId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	dispute = json.loads(request.body)
	delegate = DisputeDelegate()
	responseData = delegate.createFromJson( dispute )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	dispute = json.loads(request.body)
	delegate = DisputeDelegate()
	responseData = delegate.save( dispute )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        disputeId = requestData["id"]
        delegate = DisputeDelegate()
        responseData = delegate.delete(disputeId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = DisputeDelegate()
        responseData = delegate.getAll()
        asJson = serializers.serialize("json", responseData)
        return HttpResponse(asJson, content_type="application/json");


    # ---------------------------------------------------------
    # Single association
    # ---------------------------------------------------------
    @staticmethod
    def assignTransaction(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.assignTransaction(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignTransaction(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.unassignTransaction(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignCustomer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.assignCustomer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignCustomer(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.unassignCustomer(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.assignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignAccount(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.unassignAccount(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignPaymentCard(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.assignPaymentCard(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignPaymentCard(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = DisputeDelegate()
        responseData = delegate.unassignPaymentCard(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
