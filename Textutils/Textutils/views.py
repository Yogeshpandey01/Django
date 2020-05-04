# i have created this file- Yogesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'htmlfile.html')

def login(request):
    return render(request,'loginpage.html')

def signup(request):
    return render(request,'signupage.html')

def contactus(request):
    return render(request,'contactus.html')

def chat(request):
    return render(request,'chat.html')

def thankyou(request):
    return render(request,'thankyou.html')

def aboutus(request):
    return render(request,'aboutus.html')

def Table1(request):
    return render(request,'Table1.html')

def Terms(request):
    return render(request,'Terms.html')

def htmlfile(request):
    return render(request,'htmlfile.html')

def Charges(request):
    return render(request,'Charges.html')

def Dietplan(request):
    return render(request,'Dietplan.html')
# def analyze(request):
#     djtext = request.GET.get('text', 'default')
#     removepunc = request.GET.get('removepunc', 'off')
#     capitalize = request.GET.get('capitalize','off')
#     extraspacermv = request.GET.get('extraspacermv','off')
#
#     if removepunc =='on':
#         punctuations=''';''/"",.()^?!...—{}[]*_'''
#         analyzed=''
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#
#         params = {'analyzed_text': analyzed}
#         return render(request, 'index.html', params)
#
#     elif (capitalize =='on'):
#         analyzed =''
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#
#         params = {'analyzed_text': analyzed}
#         return render(request, 'index.html', params)
#
#     elif (extraspacermv =='on'):
#         analyzed=''
#         for index ,char in enumerate(djtext):
#             if not(djtext[index] == " " and djtext[index+1] == " "):
#                 analyzed = analyzed + char
#
#         params = {'analyzed_text': analyzed}
#         return render(request, 'index.html', params)
#
#     else:
#         return HttpResponse("Error")



# def removespaces(request):
#     return HttpResponse("extra spaces <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalized")
#
# def login(request):
#     return HttpResponse("login")