from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):

    def get(self, request, format=None):
        return Response({'hello': 'world'})


class HelloMe(APIView):

    def get(self, request, format=None):
        return Response({'hello': 'me'})

#
# # Create your views here.
# def hello_world(request):
#     return JsonResponse({'hello', 'world'})
#
#
# def hello_me(request):
#     return JsonResponse({'hello', 'me'})
