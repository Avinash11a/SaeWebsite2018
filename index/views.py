from django.shortcuts import render

def index(request):
    return render(request,'index/home.html')
def allteam(request):
    return render(request,'index/allteam.html',{})
