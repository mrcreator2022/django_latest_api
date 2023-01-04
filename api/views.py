from functools import partial
from django.shortcuts import render
from itsdangerous import Serializer
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse
import requests
import json

# Create your views here.

# @api_view(['GET'])
# def hello_word(request):
#     return Response({'msg':'hello world'})

# @api_view(['POST'])
# def hello_word(request):
#     if request.method == "POST":
#        print(request.data)
#        return Response({'msg':'hello world post req'})


# @api_view(['GET','POST'])
# def employeeapi(request):
#     if request.method == "GET":
#       return Response({'msg':'hello world Get Method'})

#     if request.method == "POST":
#       print('request.data')
#       return Response({'msg':'hello world Post Method','data':request.data})

@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def employeeapi(request,id=None):
    if request.method == "GET": 
      # id = request.data.get('id')
      if id is not None:
        employee = Employee.objects.get(id=id)
        serialize = EmployeeSerializer(employee)
        return Response({"employee": serialize.data})
      else:
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse({"employees": serializer.data}, safe=False)

    if request.method == "POST":  
      employee = EmployeeSerializer(data=request.data)
      if employee.is_valid():
        employee.save()
        return Response({'msg':'Data Created',"employee": employee.data}, status=status.HTTP_201_CREATED)
      return Response(Serializer.errors)

    if request.method == "PUT":  
      id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      serializer = EmployeeSerializer(emp, data=request.data,partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data Updated',"employee": serializer.data})
      return Response(Serializer.errors)

    if request.method == "PATCH":  
      id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      serializer = EmployeeSerializer(emp, data=request.data,partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Partial Data Updated',"employee": serializer.data})
      return Response(Serializer.errors)
    
    if request.method == "DELETE":  
      # id = request.data.get('id')
      emp = Employee.objects.get(id=id)
      emp.delete()
      return Response({'msg':'Data Deleted'})


# @api_view(['GET', 'POST'])
# def student_list(request):
#   #get all the drinks
#   #serialize them
#   #return json
#   if request.method == "GET": 
#     students = Employee.objects.all()
#     serializer = EmployeeSerializer(students, many=True)
#     return JsonResponse({"students": serializer.data}, safe=False)


#   if request.method == "POST":
#     serializer =  EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

