from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo
# Create your views here.
def index(request):
   # 1.把所有的数据查出来
   # select * from bookinfo
   books = BookInfo.objects.all()
   # 2.组织数据
   context = {
      "books":books
   }

   return render(request,'index.html',context)
   