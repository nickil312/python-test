from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request):
    return render(request,'API/index.html')
def get(request,id):
    data = [id]
    return render(request,'API/get.html',{'id':data})
def post(request):
    return render(request,'API/post.html')
def delete(request,id):
    data = [id]

    return render(request,'API/delete.html',{'id':data})
def put(request,id):
    data = [id]

    return render(request,'API/put.html',{'id':data})
# Create your views here.
