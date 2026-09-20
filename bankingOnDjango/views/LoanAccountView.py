import json

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from bankingOnDjango.delegates.LoanAccountDelegate import LoanAccountDelegate

 #======================================================================
# 
# Encapsulates data for View LoanAccount
#
# @author Harbormaster Dev Team
#
#======================================================================

#======================================================================
# Class LoanAccountView function declarations
#======================================================================
def index(request):
	return HttpResponse("Hello, world. You're at the LoanAccount index.")

    @staticmethod
    def get(request):
        requestData = json.loads(request.body)
        loanAccountId = requestData["id"]
        delegate = LoanAccountDelegate()
        responseData = delegate.get(loanAccountId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

def create(request):
	loanAccount = json.loads(request.body)
	delegate = LoanAccountDelegate()
	responseData = delegate.createFromJson( loanAccount )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

def save(request):
	loanAccount = json.loads(request.body)
	delegate = LoanAccountDelegate()
	responseData = delegate.save( loanAccount )
	asJson = serializers.serialize("json", responseData)
	return HttpResponse(asJson, content_type="application/json");

    def delete(request):
        requestData = json.loads(request.body)
        loanAccountId = requestData["id"]
        delegate = LoanAccountDelegate()
        responseData = delegate.delete(loanAccountId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    def getAll(request):
        delegate = LoanAccountDelegate()
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
        delegate = LoanAccountDelegate()
        responseData = delegate.assignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBank(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = LoanAccountDelegate()
        responseData = delegate.unassignBank(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignBranch(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = LoanAccountDelegate()
        responseData = delegate.assignBranch(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignBranch(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = LoanAccountDelegate()
        responseData = delegate.unassignBranch(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")
    @staticmethod
    def assignProduct(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = LoanAccountDelegate()
        responseData = delegate.assignProduct(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def unassignProduct(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childId = requestData["childId"]
        delegate = LoanAccountDelegate()
        responseData = delegate.unassignProduct(parentId,childId)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    # ---------------------------------------------------------
    # Multiple association
    # ---------------------------------------------------------
    @staticmethod
    def addBorrowers(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.addBorrowers(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeBorrowers(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.removeBorrowers(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addRepaymentSchedule(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.addRepaymentSchedule(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeRepaymentSchedule(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.removeRepaymentSchedule(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addPayments(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.addPayments(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removePayments(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.removePayments(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addCollateral(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.addCollateral(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeCollateral(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.removeCollateral(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


    @staticmethod
    def addFeeCharges(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.addFeeCharges(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")

    @staticmethod
    def removeFeeCharges(request):
        requestData = json.loads(request.body)
        parentId = requestData["parentId"]
        childIds = requestData["childIds"]
        delegate = LoanAccountDelegate()
        responseData = delegate.removeFeeCharges(parentId,childIds)
        asJson = serializers.serialize("json",responseData)
        return HttpResponse(asJson,content_type="application/json")


