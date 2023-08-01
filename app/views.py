from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
def fbv(request):
    return HttpResponse('<h1> this is fbv</h1>')

class cbv(View):
    def get(self,request):
        return HttpResponse('<h1> this is classbase view</h1>')
def temp_fbv(request):
    return render(request,'temp_fbv.html')

class temp_cbv(View):
    def get(self,request):
        return render(request,'temp_cbv.html')