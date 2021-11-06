from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   context = {
      "name":"志玲妹妹"
   }
   return render(request,'index.html',context)
   return HttpResponse('index')