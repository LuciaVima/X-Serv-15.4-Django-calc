from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request,num1,num2):
	resultado = int(num1) + int(num2)
	return HttpResponse('El resultado de su suma es:' + str(resultado))

def resta(request,num1,num2):
	resultado = int(num1) - int(num2)
	return HttpResponse('El resultado de su resta es:' + str(resultado))

def multiplicacion(request,num1,num2):
	resultado = int(num1) * int(num2)
	return HttpResponse('El resultado de su multiplicacion es:' + str(resultado))

def division(request,num1,num2):
	resultado = int(num1) / int(num2)
	return HttpResponse('El resultado de su division es:' + str(resultado))

def fallo(request):
	return HttpResponse('<h1><font color="red"> Not Found!</font></h1>')

